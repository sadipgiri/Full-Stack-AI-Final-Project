#!/usr/bin/env python3

"""
    top_currencies - python3 program to return top crypto currencies using coinmarketcap api
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 23 April, 2018
"""
import requests
import json

def top_crypto_prices():
    try:
        req = requests.request('GET', 'https://api.coinmarketcap.com/v1/ticker/?limit=6')
        json_data = req.json()
        return json_data
    except Exception as e:
        return offline_crypto_data() 

def offline_crypto_data():
        with open('./offline_data/top_crypto/top_crypto.json') as json_file:
                json_data = json.load(json_file)
        crypto_prices = json_data
        return crypto_prices["data"]


if __name__ == '__main__':
    print(top_crypto_prices())
    print(float(top_crypto_prices()[0]['percent_change_1h']) < 0)
    

