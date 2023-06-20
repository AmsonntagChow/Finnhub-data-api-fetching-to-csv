import finnhub
import pandas as pd
import numpy as np

finnhub_client = finnhub.Client(api_key="YOUR_KEY")

#The stock symbol of Tesla is TSLA
stock = 'AAPL'

#Transfrom Dict to DataFrame
df1 = finnhub_client.stock_insider_transactions(stock, '2020-04-01', '2023-03-31')
df = pd.DataFrame(data=df1['data'])

#Save as csv
print(df)
df.to_csv(stock+" Insider.csv", index=False)