from requests import get
import json
from pprint import pprint


""" all the weather stations url """
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902'

""" splits the stations and weathers up """
stations = get(url).json()['items']
weather = get(url).json()['items']
pprint(weather)


{
 """ ID of the station """
 'weather_stn_id': 1648902,
 """ the latitude """
 'weather_stn_lat': 52.197834,
 """the longitude"""
 'weather_stn_long': 0.125366,
 """name of the weather station"""
 'weather_stn_name': 'ACRG_ROOF'}
