#!/usr/bin/env python3

"""
    tests.py - python3 program to manually do testing as well as explore api calls or other performance calls before including those in the main program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 24th April, 2018
"""

import crypto_api


if __name__ == '__main__':
    print(crypto_api.top_crypto_prices())

"""
    Note: This is not for explicit testing since I am using python's unittests library
"""