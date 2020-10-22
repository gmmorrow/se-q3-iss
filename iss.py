#!/usr/bin/env python

__author__ = "Gabrielle"


import json
import time
import turtle
import requests
import urllib.request


astronauts = requests.get("http://api.open-notify.org/astros.json")


def astronaut_list(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


    astronaut_list(astronauts.json())
    
    parameters = {
        "lat": -4.2196,
        "lon": 170.6524
    }
    coordinates = requests.get(
    "http://api.open-notify.org/iss-now.json", params=parameters)
    astronaut_list(coordinates.json())
    return (coordinates, astronauts)


def world_map(turtle):
    turtle.Screen()
    turtle.setup(100)
    turtle.bgpic(90)
    turtle.setworldcoordinates(100)
    


    
    
    

# def main():
#     world_map()


# if __name__ == '__main__':
#     main()