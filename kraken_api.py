import base64
import hashlib
import hmac
import json
import time
import urllib.request
from datetime import datetime
import openpyxl
from websocket import create_connection

filename = 'btc_data_base.xlsx'
wb = openpyxl.load_workbook(filename=filename)
sheet = wb['Feuil1']


api_key =  "/bRc+CY6UTDE/X0q8frBaUvknG80YOdRmpokSoe4NI8kBTMaKlBlimgp"
api_sign = "W4u4lB8X9zPzjDVGcljhJjK5E+hP8m8w+6qJ+IbSiVuoRjJyQgPy9oAOOju6w8tZI9X+aBPtTDbTxYllOw8Oag=="


ws = create_connection("wss://ws.kraken.com/")
ws.send(json.dumps({ "event": "subscribe", "pair": ["XBT/EUR"],
		"subscription": { "name": "ohlc", "interval":30}}))

opened_cs = []
closed_cs = []
while True:
		result = ws.recv()
		result = json.loads(result)
		if type(result) == list:
			current_cs = result[1][1:8]
			current_cs[0] =  datetime.fromtimestamp(float(current_cs[0]))
			opened_cs.append(current_cs)
			if len(opened_cs) > 2:
				if opened_cs[-1][0] > opened_cs[-2][0]:
					closed_cs.append(opened_cs[-2])
					new_row = opened_cs[-2]
					sheet.append(new_row)
					wb.save(filename)
					opened_cs = []

ws.close()
