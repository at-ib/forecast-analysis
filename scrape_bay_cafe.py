import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import csv

# parameters
from utils import get_time_now

URL = "https://skylink-pro.com/remote-index.php?domainname=baycafe&keyword=parade"
OUTPUT_PREFIX = "bay_cafe"
OUTPUT_DIR = "ground_truth_data"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# The weather data is in <div in="col1">
page_section = soup.find(id="col2")

headers = page_section.find_all("div", class_="databoxDataHeader")
headers = [header.text for header in headers]

data = page_section.find_all("div", class_="databoxNumber")
data = [datum.text for datum in data]

output = dict(zip(headers, data))

# We also need the timestamp which is in the <h6> within the larger
# <div id="column1")>
output["page_time"] = soup.find(id="column1").find("h6").text

# Now write the data to file
time_now = get_time_now()

with open(Path(OUTPUT_DIR, f"{OUTPUT_PREFIX}_{time_now}.csv"), "w") as csvfile:
    fieldnames = list(output)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(output)
