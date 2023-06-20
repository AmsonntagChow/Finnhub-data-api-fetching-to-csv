import finnhub
import pandas as pd
import numpy as np
from datetime import datetime

finnhub_client = finnhub.Client(api_key="YOUR_KEY")

#The stock symbol
stock = 'AAPL'

#UNIX timestamp (UTC) fitting 
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 12, 31)
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())
 
#Transfrom Dict to DataFrame
df1 = finnhub_client.stock_candles(stock, '1', start_timestamp, end_timestamp)
df = pd.DataFrame(df1)

#Save as csv
print(df)
df.to_csv(stock+" Candles.csv", index=False)


#Appendix 

# resolution: Supported resolution includes 1, 5, 15, 30, 60, D, W, M .Some timeframes might not be available depending on the exchange.

# c: List of close prices for returned candles.
# h: List of high prices for returned candles.
# l: List of low prices for returned candles.
# o: List of open prices for returned candles.
# s: Status of the response. This field can either be ok or no_data.
# t: List of timestamp for returned candles.
# v: List of volume data for returned candles.