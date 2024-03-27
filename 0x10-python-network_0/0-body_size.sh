#!/bin/bash
#  This script takes in a URL, sends a request to that URL using cURL
curl -sw '%{size_download}\n' -o /dev/null "$1"
