import yfinance as yf

bank = "JPM"
system = "^GSPC"

prices = yf.download([bank, system], start="2010-01-01",
                     auto_adjust=True, progress=False)["Close"]

print(prices.head())
print(prices.tail())
print("Number of days:", len(prices))
