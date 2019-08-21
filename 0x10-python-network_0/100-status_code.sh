#!/bin/bash
#sends a request to a URL and displays only the status code of the response.
curl -sX HEAD -w "%{http_code}" "$1"
