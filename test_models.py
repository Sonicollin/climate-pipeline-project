import csv
from climate_pipeline.models import WorldBankModel
from climate_pipeline.models import GistempRecord

# good = {
#     "countryiso3code": "AFE",
#     "date": "2024",
#     "country": {"id": "ZH", "value": "Africa Eastern and Southern"},
#     "indicator": {"id": "EN.GHG.CO2.PC.CE.AR5", "value": "CO2 per capita"},
#     "value": 0.84,
# }

# print(WorldBankModel(**good))
# print(WorldBankModel(**{**good, "value": None}))
# print(WorldBankModel(**{**good, "value": -1}))

##### TEST GISTEMPRECORD MODEL ######
lines = [
    "Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON",
    "1880,-.19,-.26,-.10,-.17,-.11,-.22,-.19,-.11,-.15,-.24,-.23,-.18,-.18,***,***,-.13,-.17,-.21",
]
row = next(csv.DictReader(lines))
print(GistempRecord(**row))