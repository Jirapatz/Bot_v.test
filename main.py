import logging
import config

# from connectors.binance_futures import BinanceFuturesClient
from connectors.binance import BinanceClient
from interface.root_component import Root
from binance.cm_futures import CMFutures

cm_futures_client = CMFutures()

print(cm_futures_client.time())

cm_futures_client = CMFutures(key=config.FUTURES_API_KEY, secret=config.FUTURES_API_SECRET,base_url='https://testnet.binancefuture.com')
# Get account information
print(cm_futures_client.account())

# Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 59808
# }

# response = cm_futures_client.new_order(**params)
# print(response)


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler) 


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)
    # binance = BinanceFuturesClient(config.FUTURES_API_KEY, config.FUTURES_API_SECRET, testnet=True)
    binance = BinanceClient(config.FUTURES_API_KEY, config.FUTURES_API_SECRET, testnet=True, futures=True)
    # binance = BinanceClient(config.SPOT_API_KEY, config.SPOT_API_SECRET, testnet=True, futures=False)
    # client = Client(config.FUTURES_API_KEY, config.FUTURES_API_SECRET, testnet=True, futures=True)
    # 
    root = Root(binance)
    root.mainloop()
