#! python3

# Chapter 14 Project Fetching Current Weather Data
# Prints the weather data for a location from the command line.

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: script.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather is %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

# 09/2016 - DOES NOT WORK! This script no longer works due to changes made by
# OpenWeatherMap.org and their API access.



