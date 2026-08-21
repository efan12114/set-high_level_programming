#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of a 200 status code response
if [ $(curl -s -o /dev/null -w "%{http_code}" "$1") -eq 200 ]; then
    curl -s "$1"
fi
