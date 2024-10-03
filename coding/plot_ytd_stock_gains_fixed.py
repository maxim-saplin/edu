# filename: plot_ytd_stock_gains_fixed.py

import subprocess
import sys

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required libraries
install('pandas')
install('matplotlib')
install('yfinance')

# Now we can proceed with the main code
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbols and the start date
stocks = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-10-03'

# Fetch stock data
data = yf.download(stocks, start=start_date, end=end_date)

# Initialize YTD gains
ytd_gains = {}

# Calculate YTD gain
for stock in stocks:
    if stock in data['Adj Close']:
        initial_price = data['Adj Close'][stock].iloc[0]
        current_price = data['Adj Close'][stock].iloc[-1]
        ytd_gain = (current_price - initial_price) / initial_price * 100
        ytd_gains[stock] = ytd_gain
    else:
        ytd_gains[stock] = None  # Handle missing data

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(ytd_gains.keys(), [gain for gain in ytd_gains.values() if gain is not None], color=['blue', 'orange'])
plt.title('YTD Stock Gains for NVDA and TSLA (2024)', fontsize=14)
plt.ylabel('Percentage Gain (%)', fontsize=12)
plt.xlabel('Stocks', fontsize=12)

# Set y-limits if there's valid data
if any(gain is not None for gain in ytd_gains.values()):
    plt.ylim(min(filter(None, ytd_gains.values())) - 5, max(filter(None, ytd_gains.values())) + 5)

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.close()

print("YTD stock gains plot saved as 'ytd_stock_gains.png'.")