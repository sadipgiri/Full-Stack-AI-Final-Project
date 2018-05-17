#!/usr/bin/env python3

"""
    talk_to_mongodb - Python3 program to talk to MongoDB Server
    Created: Sadip Giri (sadipgiri@bennignton.edu)
    Date: 05/07/2018
"""

from pymongo import MongoClient

def extract_tweets(currency):
    try:
        client = MongoClient('localhost')
        database = client.crypto_studio
        collection = database.cryptos
        tweet_details = collection.find_one({'name': "{0}".format(currency)}, {'_id': 0, 'tweets': 1})
        text = ""
        for i in tweet_details['tweets']:
            text = text + " {0}".format(i['text'])
        return text
        # return tweet_details['tweets'][0]
    except Exception as e:
        print ("Unable to connect to database: {0}".format(e))

def enter_tweets(currency, tweets):
    try:
        client = MongoClient('localhost')
        database = client.crypto_studio
        collection = database.cryptos
        collection.update({'name': '{0}'.format(currency)}, {'$addToSet': {'tweets': tweets}})
    except expression as identifier:
        print("Unable to conenct to database: {0}".format(e))

def add_my_currencies(currencies):
    try:
        client = MongoClient('localhost')
        database = client.crypto_studio
        collection = database.user
        collection.update({'name': "oliver"}, {'$addToSet': {'currencies': currencies}})
        return
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def get_my_currencies():
    try:
        client = MongoClient('localhost')
        database = client.crypto_studio
        collection = database.user
        currencies = collection.find_one({'name': "oliver"}, {'_id': 0, 'currencies': 1})
        # print(currencies["currencies"])
        return currencies["currencies"]
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    # print(extract_tweets('bitcoin'))
    print(get_my_currencies()[0])