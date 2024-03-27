#!/bin/bash
# This script sends a GET request to the provided URL

curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -s "$1"
