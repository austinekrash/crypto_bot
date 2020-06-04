import pandas as pd

df = pd.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130429&end=20200520.html")[2]
df.to_excel('table.xlsx', index=False)
print('bitcoin data saved to table.xlsx')