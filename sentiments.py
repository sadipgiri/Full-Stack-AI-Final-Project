#!/usr/bin/env python3

"""
    sentiments - python3 program to return sentiments of tweets provided
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 26 April, 2018
"""

import tweets_api
from textblob import TextBlob
import re
import threading
import time
from talk_to_mongodb import extract_tweets 

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        # return 1
        return "positive"
    elif analysis.sentiment.polarity == 0:
        # return 0
        return "neutral"
    else:
        # return -1
        return "negative"

def return_sentiments(currency):
    tweets = extract_tweets(currency)
    polarity = analize_sentiment(tweets)
    # print(tweets)
    return polarity 

if __name__ == '__main__':
    s = "Numerous countries are being considered for the MEETING, but would Peace House/Freedom House, on the Border of North & South Korea, be a more Representative, Important and Lasting site than a third party country? Just asking!"
    # bitcoin_tweets = tweets_api.returnTweets("bitcoin")
    # while len(bitcoin_tweets) < 10:
    #     time.sleep(1)
    # print(analize_sentiment(tweets_api.returnTweets(bitcoin)))

    # threading.Thread().start()
    print(return_sentiments('bitcoin'))
