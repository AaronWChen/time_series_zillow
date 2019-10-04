# helper functions for cleaning data and criteria dataframe builders

import pandas as pd 
import statsmodels.api as sm 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA, ARIMA
import numpy as np
from matplotlib import pyplot as plt

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

def arima_model(data):
    """This funtion takes in a pandas series
    and the optimal AutoRegressive Integrated Moving 
    Average(ARIMA) time series model using an AR order 
    1-8(p), the differencing parameter(I) of  1 and MA(q)
    values of 1-4. It returns a statsmodel object.
    """
    
    stationarydata = data.diff().dropna().values
    model_params = {}
    lowest_bic = None
    
    for p in range(1, 8):
        for q in range(1,10):
            test_model = ARIMA(stationarydata, (p,1,q)).fit()
            test_bic = test_model.bic

            if lowest_bic is None:
                lowest_bic = test_bic
            elif lowest_bic > test_bic:
                lowest_bic = test_bic

                model_params['lowest_bic'] = lowest_bic
                model_params['p'] = p
                model_params['q'] = q
                model_params['test_model'] = test_model
            else:
                break  
    return test_model

def model_plotter(data):
    """This function takes in a pandas 
    series and plots arima model forecast and actual prices"""
    model = arima_model(data)
    forcast= model.predict(1, 300, typ='levels')
    forcast_dollars= model.predict(1, 300, typ='levels')
    plt.plot(data[0] + np.cumsum(forcast_dollars), label='predicted')
    plt.plot(data.values, label = 'actual')
    plt.legend()
    return plt.show()


    






