#!/usr/bin/python3
"""
Sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get("https://api.github.com/user",
                           auth=(argv[1], argv[2])).json()
        print(res.get("id"))
    except:
        print("Not a valid PARAMETER")
