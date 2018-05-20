#!/usr/bin/env python3

"""
    predictions.py - Python3 program to build Deep Learning LSTM prediciton model for each crypto prices
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: May 18, 2018
"""
# developing and cleaning dataset modules
import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
import numpy as np
import seaborn as sns
import json
import requests

# for building LSTM modules
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.layers import LSTM
from keras.layers import Dropout

def build_clean_dataset(crypto_symbol):
    api_endpoint = 'https://min-api.cryptocompare.com/data/histoday'
    response = requests.get(api_endpoint + '?fsym={0}&tsym=USD&limit=2000'.format(crypto_symbol))
    hist = pd.DataFrame(json.loads(response.content)['Data'])
    # to correct datetime
    hist = hist.set_index('time')
    hist.index = pd.to_datetime(hist.index, unit='s')
    hist.head()
    hist.tail()
    return hist
    
# testing it with BTC only
    hist = build_clean_dataset('BTC')

def train_test_split(df, test_size=0.1):
    split_row = len(df) - int(test_size * len(df))
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    return train_data, test_data

def build_lstm_model(input_data, output_size, neurons=20, activ_func='linear', dropout=0.50, loss='mae', optimizer='adam'):
    model = Sequential()
    model.add(LSTM(neurons, input_shape=(
              input_data.shape[1], input_data.shape[2])))
    model.add(Dropout(dropout))
    model.add(Dense(units=output_size))
    model.add(Activation(activ_func))
    model.compile(loss=loss, optimizer=optimizer)
    return model

train, test = train_test_split(hist, test_size=0.1)

def normalise_zero_base(df):
    """ Normalise dataframe column-wise to reflect changes with
        respect to first entry.
    """
    return df / df.iloc[0] - 1

def extract_window_data(df, window=7, zero_base=True):
    """ Convert dataframe to overlapping sequences/windows of
        length `window`.
    """
    window_data = []
    for idx in range(len(df) - window):
        tmp = df[idx: (idx + window)].copy()
        if zero_base:
            tmp = normalise_zero_base(tmp)
        window_data.append(tmp.values)
    return np.array(window_data)

def prepare_data(df, window=7, zero_base=True, test_size=0.1):
    """ Prepare data for LSTM. """
    # train test split
    train_data, test_data = train_test_split(df, test_size)
    
    # extract window data
    X_train = extract_window_data(train_data, window, zero_base)
    X_test = extract_window_data(test_data, window, zero_base)
    
    # extract targets
    y_train = train_data.close[window:].values
    y_test = test_data.close[window:].values
    if zero_base:
        y_train = y_train / train_data.close[:-window].values - 1
        y_test = y_test / test_data.close[:-window].values - 1
    return train_data, test_data, X_train, X_test, y_train, y_test


if __name__ == '__main__':
    train, test, X_train, X_test, y_train, y_test = prepare_data(hist)
    model = build_lstm_model(X_train, output_size=1)
    history = model.fit(X_train, y_train, epochs=10, batch_size=4)

"""
    Roadblock: its taking a lot of time! There might be memory issues if I do it for several crypto currencies
"""
    