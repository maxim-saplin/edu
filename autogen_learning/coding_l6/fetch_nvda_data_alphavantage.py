# filename: fetch_nvda_data_alphavantage.py

import requests
import pandas as pd

# Replace YOUR_API_KEY with your actual API key
API_KEY = 'YOUR_API_KEY'
symbol = 'NVDA'
function = 'TIME_SERIES_DAILY'
url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}&outputsize=compact'

response = requests.get(url)
data = response.json()

# Convert the stock data to a DataFrame
df = pd.DataFrame(data['Time Series (Daily)']).T
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Filter data for the required date range
start_date = '2024-09-01'
end_date = '2024-10-03'
df = df.loc[start_date:end_date]

print(df.head())  # Display the data