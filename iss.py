#!/usr/bin/env python

__author__ = "Gabrielle"


import json
import time
import turtle
import requests



astronauts = 'http://api.open-notify.org/astros.json'
overhead_coordinates = 'http://api.open-notify.org/iss-pass.json'
icon = 'iss.gif'
indy_map = 'map.gif'  

def astronaut_list(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    r = requests.get('astronauts')
    r.raise_for_status
    return r.text()['people']
    
    
def current_geo_coords():
    coordinates ='http://api.open-notify.org/iss-now.json'
    parameters = {
        "lat": -4.2196,
        "lon": 170.6524
    }
    r = requests.get(coordinates, params=parameters)
    r.raise_for_status()
    timestamp = r.json()['timestamp']
    coordinates = r.json()['iss_position']
    lat = float(coordinates['latitude'])
    lon = float(coordinates['longitude'])
    return time.ctime(timestamp), lat, lon

    
    # astronaut_list(coordinates.json())
    # return (coordinates, astronauts)


def world_map(lat, lon):
    map = turtle.Screen()
    map.setup(720, 360)
    map.bgpic(indy_map)
    map.setworldcoordinates(-180, -90, 180, 90)
    map.register_shape(icon)
    iss = turtle.Turtle()
    iss.shape(icon)
    iss.setheading(90)
    iss.penup()
    iss.goto(lat, lon)

    return map
    




# def main():
#     world_map()


# if __name__ == '__main__':
#     main()