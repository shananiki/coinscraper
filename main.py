import requests
import sys
from core import _loadJSON, _show_coin_data_cmc, _get_coinmarketcap_top_coins, _get_coingecko_top_coins, _show_coin_data_coingecko
from bs4 import BeautifulSoup

header = _loadJSON("header.json")

if __name__ == '__main__':
    print("----- WebScraper 1 -----")

    while True:
        print("Which market do you want to check?\n[1] Coinmarketcap\n[2] Coingecko\n[3] Exit")

        selection = input("What do you want to have?")

        if selection is "3":
            sys.exit()
        elif selection is "2":
            gecko_coins = _get_coingecko_top_coins()

            for coin in gecko_coins:
                try:
                    _show_coin_data_coingecko("https://www.coingecko.com/de/munze/{0}".format(coin.strip("\n")), header)
                except:
                    print("Some error occured.")
                print("========================================================")
        elif selection is "1":
            cmc_coins = _get_coinmarketcap_top_coins()

            for coin in cmc_coins:
                _show_coin_data_cmc("https://coinmarketcap.com/de/currencies/{0}/".format(coin), header)
                print("========================================================")


