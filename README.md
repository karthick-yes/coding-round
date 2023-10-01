# coding-round
##Kelly Leverage Calculator using Yahoo Finance Data

This Python script calculates the Kelly-Optimal Leverage for a given set of stock symbols using historical price data obtained from Yahoo Finance. The Kelly criterion is an investment strategy that maximizes the long-term growth rate of wealth and is often used to determine the optimal position size for an asset.

###Prerequisites

Before running the script, ensure you have the following Python libraries installed:

pandas\\
numpy\\
yfinance\\
You can install these libraries using pip:
pip install pandas numpy yfinance


###How to Use

The script will prompt you to enter the stock symbols you want to analyze. Provide the symbols separated by commas (e.g., "AAPL,GOOGL,MSFT").
Enter the start date and end date for the historical data in the format "YYYY-MM-DD."
Input the annualized risk-free rate as a decimal value (e.g., 0.02 for 2%).

###Output

The script will calculate and display the optimal leverage for each stock symbol provided.

###Important Notes

The risk-free rate should be an annualized value. The script will adjust it for daily calculations.
The script uses historical stock price data obtained from Yahoo Finance. Ensure you have a stable internet connection to download the data.
Error Handling

If the script encounters an error while downloading data for a particular stock symbol, it will raise a ValueError and display the reason for the failure.
Disclaimer

This script is intended for educational and informational purposes only. It does not provide financial advice or recommendations. Use the Kelly-Optimal Leverage results with caution and consider consulting with a financial advisor before making any investment decisions.

If you find any issues with the script or want to improve it, feel free to contribute and create a pull request.
