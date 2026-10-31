import numpy as np
import yfinance as yf

bank = "JPM"
system = "^GSPC"

# Download adjusted closing prices
prices = yf.download([bank, system], start="2010-01-01",
                     auto_adjust=True, progress=False)["Close"]

# Fix the column order and keep only days where both series exist
prices = prices[[bank, system]].dropna()

print(prices.head())
print(prices.tail())
print("Number of days:", len(prices))

# Daily log returns in percent
returns = 100 * np.log(prices / prices.shift(1))
returns = returns.dropna()
returns.columns = ["bank", "system"]

print(returns.head())
print(returns.describe())
