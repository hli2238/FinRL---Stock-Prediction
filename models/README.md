##Stock Prediction Project Overview:
   * In this notebook, we are using the packages pandas, os, and sklearn to train a model to predict the stock prices of S&P 500 based on the past data.

##Stock Prediction Project Walkthrough:
   * First downloads the stock data from yfinance and edits it to only use data from the past 20 years
   * The predictors are then set to only predict values in "Close", "Volume", "Open", "High", and "Low."
   * Then using the package RandomForestClassifier to train the model, the resulting model predicts the future stock changes with a 52% accuracy. 
   * To improve the accuracy, I implemented a backtesting method which can predict data in steps of 1 "year" or 250 days.
   * With the back testing, the accuracy has increased by 14% which means that the model can now predict the future changes in the stock correctly two thirds of the time

##Stock Prediction Project Run commands:
   i. predictions = backtest(sp500, model, predictors)
   ii. predictions["Predictions"].value_counts() //displays the amount of correct vs incorrect predictions
-------------------------------------------------------------------------------------------
##LSTM Model Overview:
   * In this notebook, we have implemented an LSTM model to predict from an online dataset using the packages tensorflow, pandas, os, and numpy.

##LSTM Model Walkthrough:
   * First, we imported the online dataset and assisned its data to our local variables 
   * We then implemented a function that can help us parse the data into arrays for the LSTM model
   * From here the LSTM model is initialzed by using Sequential and the learning is initialized with a lower value to test with lower learning rates. With each of the 10 runs, the error values as well as the loss values are steadily decreasing which shows that our LSTM model is becoming more accuate.
   * Using pandas packages, we then trained the model with 3 datasets, first with 60,000 rows of data, second with 5000 rows of data, and third with the remaining data. Each training result is displayed and graphed in the notebook.

##LSTM Model Run Commands (first dataset):
   i. predictions = model1.predict(X_train).flatten() 
   ii. results = pd.DataFrame(data = {'Predictions':predictions, 'Actuals':y_train})
   iii. results //displaying results vs actual from the model
   iv. plt.plot(results['Predictions'], color = 'blue')
       plt.plot(results['Actuals'], color = 'orange') // plotting the results from the model