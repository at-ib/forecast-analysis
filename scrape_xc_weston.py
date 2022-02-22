from selenium import webdriver
from selenium.webdriver.common.by import By

# parameters
URL = 'https://www.xcweather.co.uk/forecast/Weston_Super_Mare'
OUTPUT_PREFIX = 'xc_weston'


driver = webdriver.Firefox()
driver.get(URL)
forecast = driver.find_element(By.ID, "fcastbox")
