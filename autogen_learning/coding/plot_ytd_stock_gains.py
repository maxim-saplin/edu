# filename: plot_ytd_stock_gains.py

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbols and the start date
stocks = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-10-03'

# Fetch stock data
data = yf.download(stocks, start=start_date, end=end_date)

# Calculate the YTD gain
ytd_gains = {}
for stock in stocks:
    ytd_gain = (data['Adj Close'][stock][-1] - data['Adj Close'][stock][0]) / data['Adj Close'][stock][0] * 100
    ytd_gains[stock] = ytd_gain

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(ytd_gains.keys(), ytd_gains.values(), color=['blue', 'orange'])
plt.title('YTD Stock Gains for NVDA and TSLA (2024)', fontsize=14)
plt.ylabel('Percentage Gain (%)', fontsize=12)
plt.xlabel('Stocks', fontsize=12)
plt.ylim(min(ytd_gains.values()) - 5, max(ytd_gains.values()) + 5)

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.close()

print("YTD stock gains plot saved as 'ytd_stock_gains.png'.")