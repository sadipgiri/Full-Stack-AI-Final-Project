#!/usr/bin/env python3

"""
    tweets_api.py - python3 program to access tweets and return those for analyzing sentiments of any given tweeets
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 21st April, 2018
"""
import tweepy
import json
import time
from talk_to_mongodb import enter_tweets

# Specify the account credentials in the following variables:
consumer_key  = "ESrMrx02rbo92AII3Cncopxg7"
consumer_secret = "1Pgbd1UixCKFcGhRbiZeFJXaZab6wARmsObKNdVInnE9Qjd6pg"
access_token = "877199751233630208-b0XnzzRWNxliUSw5VOfPZd7bRTeuUG6"
access_token_secret = "OLOFmx8rBRHm7uknkvcN1zttIWnLczBr0aklEUbIVAG2L"


# This listener will return all Tweets it receives
class Listener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))
        
        # adding tweets to that particular currency
        # enter_tweets('bitcoin', tweet) # give the name of the currency here!!
        enter_tweets('litecoin', tweet) # give the name of the currency here!!

    def on_error(self, status):
        print(status)

def returnTweets(currency):
    # lst = []
    listener = Listener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['{0}'.format(currency)])
    # lst.append(stream.filter(track=['{0}'.format(currency)]))
    #time.sleep(10)
    # enter_tweets(currency, clean_tweet(stream.filter(track=['{0}'.format(currency)])))

if __name__ == '__main__':
    # listener = Listener()

    # # Show system message
    # print('I will now print Tweets containing "particular currency"! ==>')

    # # Authenticate
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    # # Connect the stream to our listener
    # stream = tweepy.Stream(auth, listener)
    # stream.filter(track=['Bitcoin'])
    # print(returnTweets('bitcoin'))
    print(returnTweets('litecoin'))

"""
Reference: Using Tweepy Python Package to return tweets of particular currency.
"""