#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
"""
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    main(argv)
