# Overall plan 

1. Start collecting metoffice data using the API

2. Start collecting XCWeather data by scraping it

3. Start collecting ground truth data by scraping it

4. Analyse the data

# Collecting regular data

The data sources don't seem to publish their historical forecasts. This means that I will need to take snapshots of the data at regular intervals. The first step is therefore to work out how to periodically query a website.

## Periodically querying a website

Do the scheduling using cron and the scraping using python. Cron looks very simple to use e.g. https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/, so start by working on the scraping.

## Web scraping

We'll start by scraping the [weather station data](https://skylink-pro.com/remote-index.php?domainname=baycafe&keyword=parade) following [this guide](https://realpython.com/beautiful-soup-web-scraper-python/). This is now done.

The next thing that needs scraping is the forecast data from [XCWeather](https://www.xcweather.co.uk/forecast/Weston_Super_Mare). This will be more complex than scraping the weather station data.

The remaining forecasts to gather data from for now are netweather and windguru.
## Requesting data using the Met Office API

We can get Met Office data using their [API](https://www.metoffice.gov.uk/services/data/datapoint/getting-started). This is done.