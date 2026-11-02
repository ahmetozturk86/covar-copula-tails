import numpy as np
import yfinance as yf
from pathlib import Path

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

# Sanity check: the worst days should be crises we recognise
print("\nWorst 10 days for the system:")
print(returns["system"].nsmallest(10))

print("\nWorst 10 days for the bank:")
print(returns["bank"].nsmallest(10))

# Save the returns
raw_dir = Path(__file__).parent / "raw"
raw_dir.mkdir(exist_ok=True)

file_name = f"{bank}_{system}.csv".replace("^", "")
returns.to_csv(raw_dir / file_name)
print("\nSaved to", raw_dir / file_name)
