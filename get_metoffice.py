import requests
from datetime import datetime
import json
from requests.models import Response
from api_keys import metoffice as key
from pathlib import Path

# parameters
api_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"
location_id = "354164"  # Weston-super-mare
resolution = "3hourly"
output_prefix = 'metoffice_weston'
output_dir = 'forecast_data'
file_time_format = '%Y_%m_%d_%H_%M_%S'

response = requests.get(f"{api_url}{location_id}?res={resolution}&key={key}")
output = response.json()

# Now write the data to file
time_now = datetime.now().strftime(file_time_format)

with open(Path(output_dir, f"{output_prefix}_{time_now}.json"), 'w') as jsonfile:
    json.dump(output, jsonfile, indent=4)
