#!/usr/bin/env python

# __author__ = "Gabrielle"


import requests
import time
import turtle
import json

astronauts = requests.get("http://api.open-notify.org/astros.json")

def astronaut_list(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

astronaut_list(astronauts.json())

parameters = {
    "lat": -4.2196,
    "lon": 170.6524
}
coordinates = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
astronaut_list(coordinates.json())
    

# def main():
#     astronaut_list()

# if __name__ == '__main__':
#     main()
