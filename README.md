# forecast-analysis

The aim of this project is to see which online weather forecast is the most accurate. It is motivated by the problem of choosing which forecast to look at when planning a kitesurfing trip, and will therefore initially focus on the accuracy of the forecast of wind speed and direction, and also initially focus on forecasts at the specific location of Weston-super-Mare, a popular kitesurfing spot in soutwest England.

# Data

To measure forecast accuracy we will need ground truth and forecast data.

## Ground truth data

The best known source of wind speed data for Weston-super-mare is [here](http://windwheelsandwaves.weebly.com/current-wind.html). This will need to be scraped at regular intervals.

## Forecast data

There are many online weather forecasts which are candidates for being the most accurate. Initially we will collect data from [MetOffice](https://www.metoffice.gov.uk/weather/forecast/gcjuh73jb#?nearestTo=Weston%20Super%20Mare%20(North%20Somerset)&date=2021-03-05) and [XCWeather](https://www.xcweather.co.uk/forecast/Weston_Super_Mare). For MetOffice an API is available to collect the data, whereas for XCWeather the data will probably need to be collected by scraping the html.

# Analysis

To be decided.
