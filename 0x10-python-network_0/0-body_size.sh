#!/bin/bash
# This script takes in a URL & sends a request to it
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -s "$1"
