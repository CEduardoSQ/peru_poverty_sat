from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pandas as pd
from pyreadstat import read_sav
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from peru_poverty_sat.config import INTERIM_DATA_DIR, RAW_DATA_DIR
from peru_poverty_sat.constants import ENAHO_COLS, HouseholdsCols


def extract_data(year: int, module_code: int) -> pd.DataFrame:
    """
    Extracts ENAHO data from a zipped SPSS file.

    Args:
        year: The year of the ENAHO survey.
        module_id: The code of the survey module.

    Returns:
        A pandas DataFrame with the raw ENAHO data.
    """
    module_stem: str = f"{module_code}-Modulo01"
    module_file: Path = RAW_DATA_DIR / f"{module_stem}.zip"
    data_name: str = f"Enaho01-{year}-100.sav"
    data_path: str = f"{module_stem}/{data_name}"

    print(f"Extracting {data_path} from {module_file}...")
    with ZipFile(module_file, "r") as zf:
        zf.extract(data_path, path=RAW_DATA_DIR)

    data_file = RAW_DATA_DIR / data_path
    print(f"Reading data from {data_file}...")
    df, _ = read_sav(data_file, usecols=ENAHO_COLS)

    data_file.unlink()
    (RAW_DATA_DIR / module_stem).rmdir()

    return df


def _add_key(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["year"] = enaho["AÑO"].astype("Int16")
    households["cluster"] = enaho["CONGLOME"].astype(str)
    households["house"] = enaho["VIVIENDA"].astype(str)
    households["household"] = enaho["HOGAR"].astype(str)
    return households


def _add_facade_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["plastered"] = (
        enaho["P24A"].astype("Int8").map(lambda x: 4 - x, na_action="ignore")
    )
    households["painted"] = (
        enaho["P24B"].astype("Int8").map(lambda x: 3 - x, na_action="ignore")
    )
    return households


def _add_throughface_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["paved_road"] = enaho["P25$1"].astype("boolean")
    households["dirt_road"] = enaho["P25$2"].astype("boolean")
    households["sidewalk"] = enaho["P25$3"].astype("boolean")
    households["light_pole"] = enaho["P25$4"].astype("boolean")
    return households


def _add_house_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["structure"] = (
        enaho["P101"].astype("Int8").map(
            lambda x: 8 - x, na_action="ignore").fillna(0)
    )
    households["wall"] = (
        enaho["P102"].astype("Int8").map(
            lambda x: 9 - x, na_action="ignore").fillna(0)
    )
    households["floor"] = (
        enaho["P103"].astype("Int8").map(
            lambda x: 7 - x, na_action="ignore").fillna(0)
    )
    households["roof"] = (
        enaho["P103A"].astype("Int8").map(
            lambda x: 8 - x, na_action="ignore").fillna(0)
    )
    households["rooms"] = enaho["P104"].astype("Int8").fillna(0)
    households["bedrooms"] = enaho["P104A"].astype("Int8").fillna(0)
    return households


def _add_sanitation_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["water_source"] = (
        enaho["T110"].astype("Int8").map(lambda x: 9 - x, na_action="ignore")
    )
    households["potable"] = (
        enaho["P110A1"]
        .astype("Int8")
        .map(lambda x: x == 1, na_action="ignore")
        .astype("boolean")
        .fillna(False)
    )
    households["water_treatment"] = enaho["P110A_MODIFICADA"].between(0.5, 5.0)
    households["water_access"] = (
        enaho["P110C"]
        .astype("Int8")
        .map(lambda x: x == 1, na_action="ignore")
        .astype("boolean")
    )
    households["water_access"] = (
        (enaho["P110C1"].astype("Int16") * 7)
        .where(
            households["water_access"],
            enaho["P110C2"].astype("Int16") * enaho["P110C3"].astype("Int16"),
        )
        .fillna(0)
    )
    households["toilet"] = enaho["T111A"].astype("Int8").map(
        lambda x: 11 - x,
        na_action="ignore",
    )
    return households


def _add_illumination_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["transmitted_electricity"] = enaho["P1121"].astype("boolean")
    households["wax"] = enaho["P1123"].astype("boolean")
    households["kerosene"] = enaho["P1124"].astype("boolean")
    households["generated_electricity"] = enaho["P1125"].astype("boolean")
    households["other_source"] = enaho["P1126"].astype("boolean")
    return households


def _add_combustion_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["electricity"] = enaho["P1131"].astype("boolean")
    households["petroleum"] = enaho["P1132"].astype("boolean")
    households["methane"] = enaho["P1133"].astype("boolean")
    households["coal"] = enaho["P1135"].astype("boolean")
    households["wood"] = enaho["P1136"].astype("boolean")
    households["dung"] = enaho["P1139"].astype("boolean")
    households["other_fuel"] = enaho["P1137"].astype("boolean")
    return households


def _add_assets_features(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["landline"] = enaho["P1141"].astype("boolean")
    households["phone"] = enaho["P1142"].astype("boolean")
    households["televisor"] = enaho["P1143"].astype("boolean")
    households["internet"] = enaho["P1144"].astype("boolean")
    return households


def _add_sampling_weight(
    enaho: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["sampling_weight"] = enaho["FACTOR07"].astype("float64")
    return households


def _add_georeference(
    df: pd.DataFrame, households: pd.DataFrame
) -> pd.DataFrame:
    households["longitude"] = df["LONGITUD"].astype("float64")
    households["latitude"] = df["LATITUD"].astype("float64")
    return households


def process_households(enaho: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the raw ENAHO DataFrame to create household-level features.

    Args:
        enaho: The raw ENAHO data.

    Returns:
        A DataFrame with processed household data.
    """
    df = enaho.query("RESULT == 1").copy()

    households = pd.DataFrame(index=df.index)
    households = _add_key(df, households)
    households = _add_facade_features(df, households)
    households = _add_throughface_features(df, households)
    households = _add_house_features(df, households)
    households = _add_sanitation_features(df, households)
    households = _add_illumination_features(df, households)
    households = _add_combustion_features(df, households)
    households = _add_assets_features(df, households)
    households = _add_sampling_weight(df, households)
    households = _add_georeference(df, households)

    return households.set_index(HouseholdsCols.KEY_COLS)


def calculate_wealth_index(households: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the wealth index using PCA on household features.

    Args:
        households: A DataFrame with processed household data.

    Returns:
        The input DataFrame with an added 'wealth_index' column.
    """
    df = households.copy()

    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("pca", PCA(n_components=1))]
    )

    df["wealth_index"] = pipeline.fit_transform(
        df[HouseholdsCols.FEATURES_COLS])

    return df.reset_index()


def aggregate_clusters(households: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates household data to the cluster level.

    Args:
        households_df: A DataFrame with household-level data, including a
                       'wealth_index'.

    Returns:
        A DataFrame with cluster-level aggregated data.
    """
    clusters = (
        households.groupby(["year", "cluster"])[
            ["wealth_index", "sampling_weight"] +
            HouseholdsCols.GEOREFERENCE_COLS
        ]
        .apply(
            lambda g: pd.Series(
                {
                    "wealth_index": np.average(
                        g["wealth_index"], weights=g["sampling_weight"]
                    ),
                    "longitude": g["longitude"].mean(),
                    "latitude": g["latitude"].mean(),
                    "size": len(g),
                }
            )
        )
        .astype({
            "wealth_index": "float64",
            "longitude": "float64",
            "latitude": "float64",
            "size": "int64"
        })
        .reset_index()
    )
    return clusters


def main(year: int, module_code: int):
    """
    Main function to run the ENAHO data processing pipeline.

    Args:
        year: The year of the ENAHO survey.
        module_id: The ID of the survey module.
    """
    enaho = extract_data(year=year, module_code=module_code)
    households = process_households(enaho)
    households = calculate_wealth_index(households)
    clusters = aggregate_clusters(households)

    households_path = INTERIM_DATA_DIR / "households.parquet"
    households.to_parquet(households_path, index=False)
    print(f"Processed household data saved to {households_path}")

    clusters_path = INTERIM_DATA_DIR / "clusters.parquet"
    clusters.to_parquet(clusters_path, index=False)
    print(f"Aggregated cluster data saved to {clusters_path}")


if __name__ == "__main__":
    main(year=2024, module_code=966)
