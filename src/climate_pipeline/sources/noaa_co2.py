import dlt
import csv
import requests
from pydantic import ValidationError
from climate_pipeline.models import MaunaLoaRecord

@dlt.resource(write_disposition="replace")
def mauna_loa_co2():
    url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"
    skipped = 0

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Extraction failed: {e}")
        raise

    print("Mauna Loa Extraction success!")

    lines = response.text.splitlines()
    data_lines = [line for line in lines if not line.startswith("#")]

    for row in csv.DictReader(data_lines):
        try:
            validated = MaunaLoaRecord(**row)
            yield validated.model_dump()
        except ValidationError as e:
            skipped += 1
            print(f"Skipping invalid record ({row.get('year')}, {row.get('month')}): {e}")

    print(f"Mauna Loa Extraction Done. Skipped {skipped} invalid records.")
    
        
    
    























# data_lines = [line for line in lines if not line.startswith("#")]
# print(f"{len(lines) - len(data_lines)} comment lines")
# print("\n".join(data_lines[:5]))
# print("...")
# print("\n".join(data_lines[-3:]))