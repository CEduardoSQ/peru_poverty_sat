from pathlib import Path

PROJ_DIR: Path = Path(__file__).resolve().parents[1]

DATA_DIR: Path = PROJ_DIR / 'data'
RAW_DATA_DIR: Path = DATA_DIR / 'raw'
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
