#!/usr/bin/env python

__author__ = "Gabrielle"


import json
import time
import turtle
import requests



astronauts = 'http://api.open-notify.org/astros.json'
current_coords = 'http://api.open-notify.org/iss-now.json'
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
    current_coords = 'http://api.open-notify.org/iss-now.json'
    parameters = {
        "lat": -4.2196,
        "lon": 170.6524
    }
    r = requests.get(current_coords, params=parameters)
    r.raise_for_status()
    timestamp = r.json()['timestamp']
    coordinates = r.json()['iss_position']
    lat = float(coordinates['latitude'])
    long = float(coordinates['longitude'])
    return time.ctime(timestamp), lat, long

    
    # astronaut_list(coordinates.json())
    # return (coordinates, astronauts)


def world_map(lat, long):
    map = turtle.Screen()
    map.setup(width=720, height=360)
    map.bgpic(indy_map)
    map.setworldcoordinates(-180, -90, 180, 90)
    map.register_shape(icon)
    iss = turtle.Turtle()
    iss.shape(icon)
    iss.setheading(90)
    iss.penup()
    iss.goto(lat, long)

    return map


def overhead_indy(lat, long):
    parameters = {
        "lat": 39.7684,
        "long": 86.1581
    }
    r = requests.get(overhead_coordinates, params=parameters)
    r.raise_for_status()
    time = r.json()['response'][1]['risetime']
    timestamp = time.ctime(time)
    indy = turtle.Turtle()
    indy.color("yellow")
    indy.penup()
    indy.goto(long, lat)
    indy.dot(5)
    indy.hideturtle()
    indy.write(timestamp, align='center',
    font=("Comic Sans MS", 12, "normal"))
    turtle.done()
    return timestamp


def main():
    for astro in astronauts:
        print(astro.json)

    current_iss_info = current_geo_coords()
    timestamp = current_iss_info[0]
    lat = current_iss_info[1]
    long = current_iss_info[2]
    print(f'Current ISS coordinates: lat={lat:.02f} lon={long:.02f}')
    print(f'Current ISS timestamp: {timestamp}')

    screen = None
    try:
        screen = world_map(lat, long)

        indy_lat = 39.7684
        indy_long = 86.1581
        iss_overhead_indy = overhead_indy(indy_lat, indy_long)
        print(f'Next time ISS will pass over Indy: {iss_overhead_indy}')
    except RuntimeError as err:
        print(f'ERROR: problem loading: {str(err)}')

    if screen is not None:
        print('Click on the screen to exit')
        screen.exitonclick()
    
    
    if __name__ == '__main__':
        main()