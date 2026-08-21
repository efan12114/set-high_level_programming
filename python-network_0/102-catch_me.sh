#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get "You got me!"
curl -s -L -X PUT 0.0.0.0:5000/catch_me -d "user_id=98"
