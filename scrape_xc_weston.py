from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

from constants import FORECAST_OUTPUT_DIR
from utils import get_time_now

# parameters
URL = 'https://www.xcweather.co.uk/forecast/Weston_Super_Mare'
OUTPUT_PREFIX = 'xc_weston'

driver = webdriver.Firefox()
driver.get(URL)
forecast = driver.find_element(By.ID, "fcastbox")

time_now = get_time_now()
with open(Path(FORECAST_OUTPUT_DIR, f"{OUTPUT_PREFIX}_{time_now}.txt"), 'w') as f:
    f.write(forecast.text)