#!/bin/bash
# Script to make a request that causes the server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
