import time

from Deployment.Create_Connectors_Class import Create_Connectors
from Deployment.Create_Asset_Dicts_Class import Create_Price_Refresh

from Strategies.DummyStrategy import DumbStrategy

all_config_rows = []

test_strategy = DumbStrategy()

# Get Priv Keys 
keys_dict = {
    # ALPACA PAPERTADING KEYS
    'data_provider':'Alpaca',
    'pub_key' : 'PK0RPI7F5X8M0VVED26I',
    'priv_key' :'6VoDwGzKZ3uvPPq8awfspLesuYDnPqYtx0ZhPefG',
    'api_endpoint': 'https://paper-api.alpaca.markets'
}
asseet_dict = {
    "data_provider": "Alpaca",
    "ticker": "AAPL",
    "candleSize": "1_Day"
}
connector = Create_Connectors(keys_dict)
price_data = Create_Price_Refresh(asseet_dict,connector)
obj = {
    'pricedata':price_data.fetch_price_data,
    'connector':connector,
    'asset_dict':asseet_dict
}
all_config_rows.append(obj)

while True:
  
    test_strategy.execute_trading(all_config_rows)
    print('Sleeping for 600 Seconds')
    time.sleep(600)