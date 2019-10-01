import pandas as pd
from matplotlib import pyplot as plt 

def dataframe_cleaner(df):
    """This function takes in a pandas dataframe
        and gets rid of columns with 25% percent
        of null data. It returns a dataframe"""
    
    num_nan = {}
    for col in df:
        num_nan[col]=df[col].isnull().sum()
    colums = []
    for colum,nan in sorted(num_nan.items(), key = lambda x:x[1], reverse=True):
        if nan < 0.25*len(df[colum]):
            colums.append(colum)
    return df[colums] 
    

def return_plotter(df):
    """This function takes in a pandas dataframe and 
        a list of zipcodes. It returns a line plotter
        for top five zipcodes with the highest return."""
    
    df_return = df.pct_change()

    yr_returns = {}
    for i in df_return:
        yr_returns[i] = df_return[i].mean()

    sorted_yr_returns = sorted(yr_returns.items(), key = lambda x: x[1], reverse=True)
    top_five = sorted_yr_returns[:5]

    for zipcode, retur in top_five:
        df_return[zipcode].plot()
        plt.legend()
    return plt.show()

def name_zipcode_area(df, zipcodes):
    """This function takes in a pandas dataframe
        and a list of zipcodes and, returns a dataframe."""
    
    if len(zipcodes) == 1:
        return df[df['RegionName']==zipcodes]
    else:
        concat_df = [df[df['RegionName']==i] for i in zipcodes]
        df = pd.concat(concat_df)
        return df
        
    

         


        