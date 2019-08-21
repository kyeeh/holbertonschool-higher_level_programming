#!/bin/bash
#Sends a JSON POST request to a URL passed as the first argument
curl -sX POST --data @"$2" --header "Content-Type: application/json" "$1"
