import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# parameters
url = 'https://www.xcweather.co.uk/forecast/Weston_Super_Mare'
output_prefix = 'xc_weston_'
output_dir = 'forecast_data/'
file_time_format = '%Y_%m_%d_%H_%M_%S'

page = requests.get(url, timeout=(3.05, 1))

soup = BeautifulSoup(page.content, 'html.parser')

# The weather data is in <div id="fcastbox">
page_section = soup.find(id='fcastbox')