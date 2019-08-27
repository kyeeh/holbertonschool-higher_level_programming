#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter
"""
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], email)
    with request.urlopen(req) as res:
        print(res.read().decode("utf8"))
