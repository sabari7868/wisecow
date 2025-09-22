#!/usr/bin/env python3
import requests

URL = "http://localhost:4499"  # Replace with your app URL

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print(f"Application is UP! ({URL})")
    else:
        print(f"Application is DOWN! Status code: {response.status_code}")
except requests.RequestException:
    print(f" Application is DOWN! Could not connect to {URL}")

