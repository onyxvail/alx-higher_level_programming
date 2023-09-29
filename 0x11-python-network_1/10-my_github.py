#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get('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',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
