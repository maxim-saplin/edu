# filename: fetch_nvda_data.py

import pandas_datareader as pdr
from datetime import datetime

start = datetime(2024, 9, 1)
end = datetime(2024, 10, 3)

# Fetch data for Nvidia (NVDA)
data = pdr.get_data_yahoo('NVDA', start=start, end=end)

print(data.head())  # Check the first few rows