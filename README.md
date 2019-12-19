# Making Predictions with Time Series Data

## Author: 
### Aaron Washington Chen [GitHub](https://github.com/AaronWChen)


## Executive Summary
This project sought the 5 best zipcodes for short-term (<5 year turnaround) real estate investments based off of Zillow sales data.

The primary suggestion at minimum viable product (MVP) delivery in September 2019 was to [avoid](https://www.investopedia.com/investing/next-housing-recession-2020-predicts-zillow/) investing in real estate due to market conditions (over valued) and market predictions ([likely recession](http://zillow.mediaroom.com/2018-05-22-Experts-Predict-Next-Recession-Will-Begin-in-2020)).

If the client insisted on investing in real estate, the 5 zipcodes/areas recommended with estimated conservative returns at the end of 2021 were:
1. Benson, NC 27504 ($~50k on ~$150k purchase)
2. Centerville, TN 37033 ($~20k on ~$85k purchase)
3. Austin, TX 78758 (~$53k on ~$300k purchase)
4. Cedar Creek, TX 78612 (~$72k on ~$212k purchase)
5. Charlotte, NC 28208 (~$32k on ~$125k purchase)

[Summary Presentation](https://drive.google.com/open?id=1NprmQa0j-SuBJF2Hp1D3n5trHvHh7ka2OdE29vGjBuE)


## Project Information
As a consultant for a real estate investment firm, I was asked to answer the following question in 5 days: 
> What are the top 5 best zipcodes for us to invest in?

The original data came from [Zillow Research](https://www.zillow.com/research/data/) but has been included in this repo in the data folder as ```zillow_data.csv```

Because of the large number of records to potentially analyze (~15,000 zipcodes), it was logistically impossible to do a complete and accurate prediction for each zipcode in the time window. 

Instead, I looked at the work and comments of experts who have a lot more data than I do. Using several [other](https://www.zillow.com/research/local-market-reports/) [Zillow](https://www.zillow.com/research/home-searches-potential-moves-13192/) [articles](http://zillow.mediaroom.com/2018-01-09-San-Jose-and-Raleigh-are-Zillows-Hottest-Housing-Markets-for-2018), I narrowed down the search to areas that have been generating a lot of search and interest requests on Zillow's own servers. This reduced the zipcodes of interest down to a few hundred.

To perform the predictions, I used Facebook's Prophet library inside Jupyter Notebooks to display data tables and generate visualizations faster and more intuitively than with scripts.

A short turnaround time for investment was chosen because the predictions became too unreliable much further into the future.


## Improvements and Next Steps
With a few metropolitan areas and several hundred zipcodes predicted, some next steps could involve refactoring the code to use individualized Auto Regressive Integrated Moving Average (ARIMA) models to perform the predictions. However, each zipcode would require a custom-tuned ARIMA model and this amount of time investment may not be worth it, depending on client wishes.


## Running the Code
If you are looking to run and/or work on this project yourself, you will need to:
1. Install Python 3 (I prefer and recommend [Anaconda](https://www.anaconda.com/distribution/))
2. [Install PyStan](https://pystan.readthedocs.io/en/latest/installation_beginner.html)
3. [Install Facebook Prophet](https://facebook.github.io/prophet/docs/installation.html)
4. Clone [this repo](https://github.com/AaronWChen/time_series_zillow)
5. Install the packages in ```requirements.txt``` via pip (```pip install -r requirements.txt``` from the command line)

If you want to see the high level summary, the presentation slides and presenter notes are all that are necessary. However, feel free to peruse the Jupyter Notebook files generated for each metropolitan area inside the python directory.

If you are looking to make changes to the code, I recommend using Visual Studio Code to open the files and edit.