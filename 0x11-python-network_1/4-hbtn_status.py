#!/usr/bin/python3
'''a Python script that fetches https://alx-intranet.hbtn.io/status
with package requests
'''

import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r.text))
