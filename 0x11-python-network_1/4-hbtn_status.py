#!/usr/bin/python3
"""Script that Fetches https://intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":

    with requests.get('https://intranet.hbtn.io/status') as resp:
        body = resp.text
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
