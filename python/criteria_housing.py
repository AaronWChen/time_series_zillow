import pandas as pd
from matplotlib import pyplot as plt 


def dataframe_aggregator(df, zipcodes):
    """This function takes in a pandas dataframe
        and a list of zipcodes and, returns a dataframe."""
    
    if len(zipcodes) == 1:
        return df[zipcodes]
    else:
        concat_df = [df[zipcodes] for i in zipcodes]
        df = pd.concat(concat_df)
        return df
    

def name_zipcode_area(df, zipcodes):
    """This function takes in a pandas dataframe
        and a list of zipcodes and, returns a dataframe."""
    
    if len(zipcodes) == 1:
        return df[df['RegionName']==zipcodes]
    else:
        concat_df = [df[df['RegionName']==i] for i in zipcodes]
        df = pd.concat(concat_df)
        return df      


        