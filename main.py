import logging
import config

# from connectors.binance_futures import BinanceFuturesClient
from connectors.binance import BinanceClient
from interface.root_component import Root


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
    # print("API_KEY: ", config.SPOT_API_KEY)
    # print("API_SECRET: ", config.SPOT_API_SECRET)
    
    root = Root(binance)
    root.mainloop()
