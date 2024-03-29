#!/bin/bash
# Script to send a JSON POST request to a URL and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
