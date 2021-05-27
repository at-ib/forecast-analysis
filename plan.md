# Overall plan 

1. Start collecting metoffice data using the API

2. Start collecting XCWeather data by scraping it

3. Start collecting ground truth data by scraping it

4. Analyse the data

# Collecting regular data

The data sources don't seem to publish their historical forecasts. This means that I will need to take snapshots of the data at regular intervals. The first step is therefore to work out how to periodically query a website.

## Periodically querying a website

Do the scheduling using cron and the scraping using python