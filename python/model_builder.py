import pandas as pd 
import statsmodels.api as sm 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA, ARIMA
import numpy as np

def stationarity_test(df, conversion):
    """This function takes in a pandas dataframe
        and runs a time series stationary test. 
        It returns the name of the columns....
        Dude stop bugging me!"""

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
                test_stationary.append((col, i, adf_))
        return [(i[0], i[1], i[2])for i in test_stationary if i[2] <0.20]



