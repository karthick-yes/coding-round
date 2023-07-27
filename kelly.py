import pandas as pd
import numpy as np
from numpy.linalg import inv
import yfinance as yf
from typing import Set, Dict
from datetime import date


def calc_kelly_leverages():
    
    stocks = input("Enter the stock symbols (separated by commas): ").split(',')
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    risk_free_rate = float(input("Enter the risk-free rate: "))

    """
    IMP: risk_free_rate is annualized
    """
    stock_data = {}
    dailyret = {}
    excessDailyRet = {}
    result = {}

    for symbol in stocks:
        try:
            ticker = yf.Ticker(symbol)
            hist_prices = ticker.history(start=start_date, end=end_date)
            stock_data[symbol] = pd.DataFrame(hist_prices)  # Convert to DataFrame
        except Exception as e:
            raise ValueError(f'Unable to download data for {symbol}. '
                             f'Reason: {str(e)}')

        # calculating daily returns
        dailyret[symbol] = stock_data[symbol]["Close"].pct_change()
        # calculating excess daily returns
        excessDailyRet[symbol] = (dailyret[symbol] - (risk_free_rate / 252))

        df = pd.DataFrame(excessDailyRet[symbol]).dropna()
        # Calculate the CoVariance and Mean of the DataFrame
        C = 252 * df.cov()
        M = 252 * df.mean()
        # Calculate the Kelly-Optimal Leverages using Matrix Multiplication
        F = inv(C).dot(M)
        result[symbol] = F[0]

    return result

leverages = calc_kelly_leverages()
for symbol, leverage in leverages.items():
    print(f"Optimal Leverage for {symbol}: {leverage}")



        



        



     
        

    

        
    
