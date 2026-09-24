# TODO / Project Log

A portfolio project extending the weather-pipeline-project curriculum: a multi-source climate data pipeline, deployed against a real cloud warehouse (Snowflake), with a public-facing dashboard.

## Setup

- [x] Scaffold `src/climate_pipeline/` package layout with a `sources/` subfolder for per-source extraction code
- [x] Set up `pyproject.toml` as the single dependency source (no separate `requirements.txt`)
- [x] Initialize Git repo, `.gitignore`, and push to GitHub

## Data sources

- [ ] **World Bank Indicators API** — CO2 emissions per capita by country (`EN.ATM.CO2E.PC`). Genuine REST/JSON source; requires handling real pagination (unlike the single-response Open-Meteo calls from the last project).
- [ ] **NOAA Mauna Loa CO2 record** — flat-file time series (the "Keeling Curve"). First file-based (non-REST) extraction pattern.
- [ ] **NASA GISTEMP** — global temperature anomaly dataset, flat CSV, different structure from NOAA's.
- [ ] **NOAA GHCN** — daily station-level temperature data. Large, genuinely messy (missing readings, station changes over time).

## Validation & modeling

- [ ] Pydantic contract per source (`models.py`), reflecting each source's real shape and plausible-value constraints
- [ ] dbt staging models — one per source, light cleaning only
- [ ] dbt intermediate models — align sources onto a common time/geography grain
- [ ] dbt mart models — analysis-ready tables (e.g. global temp anomaly vs. CO2 by year, regional warming rates)
- [ ] dbt tests across all layers
- [ ] `dbt docs generate` — produce and publish the auto-generated docs/lineage site

## Infrastructure

- [ ] Dockerize the pipeline
- [ ] Set up `docker-compose.yml` with persistent volume for local output
- [ ] Airflow DAG(s) — likely more than one, given sources update on different schedules
- [ ] GitHub Actions CI — build + test on push
- [ ] GitHub Actions secrets — store Snowflake credentials securely, never committed

## Snowflake

- [ ] Sign up for Snowflake free trial
- [ ] Configure `dlt` Snowflake destination (alongside DuckDB, likely toggled via an environment variable)
- [ ] Configure dbt multi-target `profiles.yml` (`dev` = DuckDB, `prod` = Snowflake)
- [ ] Confirm warehouse auto-suspend is set correctly (avoid burning trial credits)

## Dashboard

- [ ] Streamlit app exploring temperature anomaly vs. CO2 concentration over time, filterable by region
- [ ] Deploy dashboard somewhere publicly viewable

## Documentation

- [ ] README explaining architecture, design decisions, and tradeoffs (not just setup instructions)
