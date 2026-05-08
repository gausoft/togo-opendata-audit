"""
Fetch all dataset metadata from opendata.gouv.tg via paginated API.
Output: data/raw/datasets_metadata.json (full uData payload per dataset).
"""
import json
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

BASE = "https://opendata.gouv.tg/api/1/datasets/"
PAGE_SIZE = 100
OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "datasets_metadata.json"


def fetch(url: str, retries: int = 3) -> dict:
    headers = {"User-Agent": "togo-opendata-audit/1.0", "Accept": "application/json"}
    for attempt in range(retries):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except (HTTPError, URLError, TimeoutError) as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    return {}


def main() -> None:
    all_datasets: list[dict] = []
    page = 1
    while True:
        url = f"{BASE}?page={page}&page_size={PAGE_SIZE}"
        print(f"Page {page}...", flush=True)
        data = fetch(url)
        items = data.get("data", [])
        if not items:
            break
        all_datasets.extend(items)
        total = data.get("total", 0)
        print(f"  fetched {len(items)} (cumulative {len(all_datasets)} / {total})", flush=True)
        if len(all_datasets) >= total:
            break
        page += 1
        time.sleep(0.3)

    OUT_FILE.write_text(json.dumps(all_datasets, ensure_ascii=False, indent=2))
    print(f"\nWrote {len(all_datasets)} datasets to {OUT_FILE}")


if __name__ == "__main__":
    main()
