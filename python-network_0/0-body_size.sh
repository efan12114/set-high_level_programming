#!/bin/bash
# Takes in a URL, sends a request, and displays the size of the body of the response in bytes
curl -sso /dev/null -w '%{size_download}\n' "$1"
