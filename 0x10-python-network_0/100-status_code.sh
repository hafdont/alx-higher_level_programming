#!/bin/bash
# Script to send a request to a URL and display the status code of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
