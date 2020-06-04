
from datetime import datetime

import pandas as pd
import schedule

def saving_data():
    df = pd.read_html(
        "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130429&end=20200520.html")[2]
    df.to_excel('table.xlsx', index=False)

schedule.every().day.at("02:36").do(saving_data)

while True:
    schedule.run_pending()