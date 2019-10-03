# helper functions for cleaning data and criteria dataframe builders

import pandas as pd 
import statsmodels.api as sm 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA, ARIMA
import numpy as np

def dataframe_cleaner (df):
    """Takes in a pandas dataframe and 
        removes all the columns with null values
        and returns a pandas dataframe"""
    columns = []
    for col in df:
        if (df[col].isnull().sum()) == 0:
            columns.append(col)
    return df[columns]

def stationarity_test(df, conversion):
    """This function takes in a pandas dataframe
        and runs a time series stationary test. 
        It returns a tuple with value of
        adfuller p-score and the n
        conversion in the case of diff() and 
        conversion : {'pct_change', 'diff()'}"""
    assert isinstance(conversion, str), 'Second argument needs to be a string'

    if conversion == 'pct_change()':
        stationary_test = []
        for j in range(1,10):
            adf_df = adfuller(df.pct_change(j).dropna())[1]
            if adf_ < 0.05:
                stationary_test.append((i, adf_df))
                break 
        return stationary_test

    elif conversion == 'diff()':
        test_stationary = []
        for i in range(1, 10):
            adf_ = adfuller(df.diff(i).dropna())[1]
            if adf_ < 0.05:
                test_stationary.append((i, adf_))
                break 
        return test_stationary

def model(df):
    """Takes in a stationary pandas series and
        gives back ARIMA model for your series"""
    
    model_params = []
    model_lowestbic = []
    
    for p in range(1,3):
        for q in range(1,3):
            test_model = ARIMA(df, (p,0,q)).fit()
            test_bic = test_model.bic
            model_params.append((p, q, test_model, test_bic))
    for tup in model_params:
        model_lowestbic.append(tup[3])
        
    lowest_bic = min(model_lowestbic)
    for tup in model_params:
        if tup[3]==lowest_bic:
            return tup[2].plot_predict(1, 275)





