import requests
import json
from api_keys import metoffice as key
from pathlib import Path

from constants import FORECAST_OUTPUT_DIR
from utils import get_time_now

# parameters
URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"
LOCATION_ID = "354164"  # Weston-super-mare
RESOLUTION = "3hourly"
OUTPUT_PREFIX = 'metoffice_weston'

response = requests.get(f"{URL}{LOCATION_ID}?res={RESOLUTION}&key={key}")
output = response.json()

# Now write the data to file
time_now = get_time_now()
with open(Path(FORECAST_OUTPUT_DIR, f"{OUTPUT_PREFIX}_{time_now}.json"), 'w') as jsonfile:
    json.dump(output, jsonfile, indent=4)
