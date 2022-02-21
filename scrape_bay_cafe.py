import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import csv

# parameters
url = 'https://skylink-pro.com/remote-index.php?domainname=baycafe&keyword=parade'
output_prefix = 'bay_cafe'
output_dir = 'ground_truth_data'
file_time_format = '%Y_%m_%d_%H_%M_%S'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# The weather data is in <div in="col1">
page_section = soup.find(id='col2')

headers = page_section.find_all('div', class_='databoxDataHeader')
headers = [header.text for header in headers]

data = page_section.find_all('div', class_='databoxNumber')
data = [datum.text for datum in data]

output = dict(zip(headers, data))

# We also need the timestamp which is in the <h6> within the larger 
# <div id="column1")>
output["page_time"] = soup.find(id='column1').find('h6').text

# Now write the data to file
time_now = datetime.now().strftime(file_time_format)

with open(Path(output_dir, f"{output_prefix}_{time_now}.csv"), 'w') as csvfile:
    fieldnames = list(output)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(output)
