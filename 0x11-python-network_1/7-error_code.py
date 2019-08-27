#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get(argv[1])
        res.raise_for_status()
        print(res.text)
    except:
        print("Error code: {}".format(res.status_code))
