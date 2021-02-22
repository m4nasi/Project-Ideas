from requests import get
import json
from pprint import pprint
from haversine import haversine

""" Finds the data of different weather stations """
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

""" set a latitude and a longitude """
my_lat = 52.194504
my_lon = 0.134708

""" finds and splits all the weather stations """
all_stations = get(stations).json()['items']


""" function to find the closest weather station """
def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()

weather = weather + str(closest_stn)

my_weather = get(weather).json()['items']
pprint(my_weather)
