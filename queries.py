import duckdb

conn = duckdb.connect("output/climate_pipeline.duckdb")
world_bank_result = conn.sql("SELECT * FROM climate_data.co2_emissions_per_capita LIMIT 10")
print(world_bank_result)
noaa_co2_result = conn.sql("SELECT * FROM climate_data.mauna_loa_co2")
print(noaa_co2_result)
gistemp_result = conn.sql("SELECT * FROM climate_data.gistemp_temperature_anomalies")
print(gistemp_result)
