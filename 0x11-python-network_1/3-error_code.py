#!/usr/bin/python3
"""
Sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
