#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":

    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        body = resp.read()
        print('Body response:')
        print('    - type: {}'.format(type(body)))
        print('    - content: {}'.format(body))
        print('    - utf8 content: {}'.format(body.decode("utf-8")))
