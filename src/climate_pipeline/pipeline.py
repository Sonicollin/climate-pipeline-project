import dlt
import os
from climate_pipeline.sources.world_bank import co2_emissions_per_capita
from climate_pipeline.sources.noaa_co2 import mauna_loa_co2
from climate_pipeline.sources.nasa_gistemp import gistemp_temperature_anomalies

os.makedirs("output", exist_ok=True)

def run(refresh: str | None = None):
    pipeline = dlt.pipeline(
        pipeline_name="climate_pipeline",
        destination=dlt.destinations.duckdb("output/climate_pipeline.duckdb"),
        dataset_name="climate_data"
    )

    load_info = pipeline.run([co2_emissions_per_capita, 
                              mauna_loa_co2, 
                              gistemp_temperature_anomalies],
                                refresh=refresh)
    print(load_info)

if __name__ == "__main__":
    run()