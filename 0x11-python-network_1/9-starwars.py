#!/usr/bin/python3
"""
Sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get("https://swapi.co/api/people/?search={}".
                           format(argv[1])).json()
        print("Number of results: {}".format(res["count"]))
        for person in res["results"]:
            print(person["name"])
    except:
        print("Not a valid PARAMETER")
