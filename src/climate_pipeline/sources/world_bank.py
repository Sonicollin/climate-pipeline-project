import dlt
import requests
import time
from pydantic import ValidationError
from climate_pipeline.models import WorldBankModel

@dlt.resource(write_disposition="replace")
def co2_emissions_per_capita():
    url = "https://api.worldbank.org/v2/country/all/indicator/EN.GHG.CO2.PC.CE.AR5"
    page = 1
    max_retries = 3
    skipped = 0

    while True:
        params = {"format": "json", "per_page": 1000, "page": page}

        for attempt in range(1, max_retries + 1):
            try:
                response = requests.get(url, params=params, timeout=15)
                metadata, records = response.json()
                break
            except requests.exceptions.RequestException as e:
                print(f"Page {page}, attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    raise
                time.sleep(2 * attempt)

        print(f"Fetched page {page} of {metadata['pages']} ({len(records)} records)")

        for record in records:
            try:
                validated = WorldBankModel(**record)
                yield validated.model_dump()
            except ValidationError as e:
                skipped += 1
                print(f"Skipping invalid record ({record.get('countryiso3code')}, {record.get('date')}): {e}")

        if page >= metadata["pages"]:
            break

        page += 1

    print(f"World Bank Extraction Done. Skipped {skipped} invalid records.")