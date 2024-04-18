Project Overview:
In this notebook, we are using the packages pandas, os, and sklearn to train a model to predict the stock prices of S&P 500 based on the past data.

Project Walkthrough:
   * First downloads the stock data from yfinance and edits it to only use data from the past 20 years
   * The predictors are then set to only predict values in "Close", "Volume", "Open", "High", and "Low."
   * Then using the package RandomForestClassifier to train the model, the resulting model predicts the future stock changes with a 52% accuracy. 
   * To improve the accuracy, I implemented a backtesting method which can predict data in steps of 1 "year" or 250 days.
   * With the back testing, the accuracy has increased by 14% which means that the model can now predict the future changes in the stock correctly two thirds of the time

Project Run commands:
   i. predictions = backtest(sp500, model, predictors)
   ii. predictions["Predictions"].value_counts() //displays the amount of correct vs incorrect predictions

