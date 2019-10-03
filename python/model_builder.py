# helper functions for cleaning data and criteria dataframe builders

import pandas as pd 
import statsmodels.api as sm 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA, ARIMA
import numpy as np

def stationarity_test(df, conversion):
    """This function takes in a pandas dataframe
        and runs a time series stationary test. 
        It returns a tuple name of the columns, value of
        conversion in the case of diff() and value of
        adfuller p-score.
        conversion : {'pct_change', 'diff()'}"""
    assert isinstance(df, pd.DataFrame), 'First argument needs to be a dataframe'
    assert isinstance(conversion, str), 'Second argument needs to be a string'

    if conversion == 'pct_change()':
        stationary_test = []
        for col in df:
            adf_df = adfuller(df[col].pct_change().dropna())[1]
            stationary_test.append((col, adf_df))
        return stationary_test

    elif conversion == 'diff()':
        test_stationary = []
        for col in df:
            for i in range(1, 10):
                adf_ = adfuller(df[col].diff(i).dropna())[1]
                if adf_ < 0.05:
                    test_stationary.append((col, i, adf_))
                    break
        return test_stationary

    




