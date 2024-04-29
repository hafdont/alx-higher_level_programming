#!/usr/bin/python3
"""
Sends a request to the given URL and displays t variable in the response header
"""

import urllib.request
import sys

if __name__ == "__main__":
     url = sys.argv[1]
     with urllib.request.urlopen(url) as response:
         request_id = response.getheader('X-Request-Id')
         print(request_id)
