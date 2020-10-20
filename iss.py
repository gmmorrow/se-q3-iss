#!/usr/bin/env python

# __author__ = "Gabrielle"


import requests
import time
import turtle
import json

response = requests.get("http://api.open-notify.org/astros.json")

def astronaut_list(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

astronaut_list(response.json())

# def main():
#     astronaut_list()

# if __name__ == '__main__':
#     main()
