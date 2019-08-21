#!/bin/bash
#Makes a request to 0.0.0.0:5000/catch_me to get it!
curl -sLX PUT --data "user_id=98" --header "origin:HolbertonSchool" 0.0.0.0:5000/catch_me
