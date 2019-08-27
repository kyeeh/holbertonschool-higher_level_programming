#!/usr/bin/python3
"""
Sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get("https://swapi.co/api/people/?search={}".
                       format(argv[1])).json()
    print("Number of results: {}".format(res["count"]))
    for person in res["results"]:
        print(person["name"])
    while res["next"] is not "null":
        res = requests.get(res["next"]).json()
        for person in res["results"]:
            print(person["name"])
