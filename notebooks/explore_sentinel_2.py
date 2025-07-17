# %%
import concurrent.futures
import logging

import ee
import pandas as pd
import requests

from tqdm import tqdm

from peru_poverty_sat.config import INTERIM_DATA_DIR, PROCESSED_DATA_DIR

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# %%
ee.Authenticate()
ee.Initialize(project='peru-poverty-sat')

# %%
clusters_file = INTERIM_DATA_DIR / 'clusters.parquet'
clusters = pd.read_parquet(clusters_file)

# %%
dataset_dir = PROCESSED_DATA_DIR / 'ENAHOS2'
clusters['filename'] = clusters.apply(
    lambda row: f"{row['year']}_{row['cluster']}", axis=1
)
points = list(zip(
    clusters['longitude'],
    clusters['latitude'],
    clusters['filename']
))

# %%
def download_image(lon: float, lat: float, filename: str) -> bool:
    region = ee.Geometry.Point((lon, lat)).buffer(1120).bounds()
    image = (
        ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
        .filterDate('2024-01-01', '2024-12-31')
        .filterBounds(region)
        .filter(ee.Filter.lt('CLOUD_COVERAGE_ASSESSMENT', 20))
        .map(lambda img: img.updateMask(img.select('QA60').eq(0)))
        .select(['TCI_R', 'TCI_G', 'TCI_B'])
        .sort('CLOUD_COVERAGE_ASSESSMENT')
        .median()
    )
    if not image.getInfo():
        raise FileNotFoundError(f"No Earth Engine image found for coordinates ({lon}, {lat}).")

    url = image.getThumbUrl({
        'dimensions': 224,
        'region': region,
        'format': 'png',
        'min': 0,
        'max': 255
    })

    response = requests.get(url)

    if response.status_code == 200:
        image_file = dataset_dir / 'images' / f"{filename}.png"
        with open(image_file, 'wb') as f:
            f.write(response.content)
        return True
    else:
        raise requests.exceptions.HTTPError(f"Failed to download image from {url}. Status code: {response.status_code}")

# %%
MAX_WORKERS = 10

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    future_to_point = {
        executor.submit(download_image, lon, lat, filename): (lon, lat, filename)
        for lon, lat, filename in points
    }

    for future in tqdm(
        concurrent.futures.as_completed(future_to_point),
        total=len(points),
        desc="Downloading images"
    ):
        lon, lat, filename = future_to_point[future]
        try:
            future.result()
        except FileNotFoundError as e:
            logging.error(f"Failed to download image for {filename}: {e}")
        except requests.exceptions.HTTPError as e:
            logging.error(f"Failed to download image for {filename}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while downloading image for {filename}: {e}")


# %%
index_file = dataset_dir / 'index.parquet'
clusters.to_parquet(index_file)
