#!/usr/bin/python3
'''a Python script that takes in a URL and an email,
sends a POST request to the passed  URL with the email
as a parameter, and displays the body of the response'''

import requests
import sys

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
    # print("Your email is: {}".format(sys.argv[2]))
