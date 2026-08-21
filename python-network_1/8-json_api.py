#!/usr/bin/python3
"""Sends a POST request to search_user endpoint with a letter parameter"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        data = r.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
