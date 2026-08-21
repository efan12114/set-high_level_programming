#!/usr/bin/python3
"""Displays X-Request-Id header variable from a request"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
