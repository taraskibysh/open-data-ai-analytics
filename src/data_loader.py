import requests
from pathlib import Path

DATA_URL = "https://data.gov.ua/dataset/1077e470-bfcb-434e-ab41-1a95c1f527ce/resource/dbfcbad0-3fc9-41b2-a5ad-5c7f25dbacda/download/publichna-informatsiia-vikhidni-za-gruden-2025.xlsx"

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FILE_PATH = DATA_DIR / "publichna-informatsiia-vikhidni-za-gruden-2025.xlsx"

def download_dataset(url: str, path: Path):
    print(f"Downloading dataset from {url} ...")
    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    print(f"Dataset saved to {path}")

if __name__ == "__main__":
    download_dataset(DATA_URL, FILE_PATH)