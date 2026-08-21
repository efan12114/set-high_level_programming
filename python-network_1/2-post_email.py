#!/usr/bin/python3
"""Sends a POST request to a given URL with an email parameter"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=payload)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
