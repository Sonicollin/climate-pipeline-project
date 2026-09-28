import dlt
import csv
import requests
from pydantic import ValidationError
from climate_pipeline.models import GistempRecord

@dlt.resource(write_disposition="replace")
def gistemp_temperature_anomalies():
    url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    skipped = 0

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Extraction failed!: {e}")
        raise

    print("GISTEMP Extraction Success!")

    lines = response.text.splitlines()
    data_lines = lines[1:] # Skips title line of CSV

    for row in csv.DictReader(data_lines):
        try:
            validated = GistempRecord(**row)
            yield validated.model_dump()
        except ValidationError as e:
            skipped += 1
            print(f"Skipping invalid record ({row.get('Year')}): {e}")

    print(f"Gistemp Extraction Complete. Skipped {skipped} invalid records.")




# print(f"{len(lines)} lines total")
# print("\n".join(lines[:4]))
# print("...")
# print("\n".join(lines[-3:]))