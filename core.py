import json
from typing import List
import requests
from bs4 import BeautifulSoup

#paar Funktionen die gebraucht werden könnten

def _loadJSON(filename)-> json:
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
        return data

#Coinmarketcap (CMC) funktionen

def _get_coinmarketcap_top_coins()-> 'list':
    url = "https://coinmarketcap.com/de/"
    header = _loadJSON("header.json")
    req = requests.get(url, header)
    soup = BeautifulSoup(req.content, 'html.parser')

    #Current Value
    coins = soup.find_all("p", class_="sc-1eb5slv-0 iJjGCS")

    coin_list = []

    for coin in coins:
        coin_list.append(coin.get_text().lower().replace(" ", "-"))
    
    return coin_list

def _show_coin_data_cmc(url, header)-> 'print':

    coin_name = url.split("/")
    print("Coin:\t{0}".format(coin_name[len(coin_name)-2]))

    req = requests.get(url, header)
    soup = BeautifulSoup(req.content, 'html.parser')


    #Current Value
    print("Current Value:\t{0}".format(soup.find("div", class_="priceValue___11gHJ").get_text()))

    #Marketcap, Full MarketCap, 24h Volume, Volume/MarketCap, Supply
    coin_data = soup.find_all("div", class_="statsValue___2iaoZ")
    #for data in coin_data:
    #    print(data.get_text())
    
    print("MarketCap:\t{0}".format(coin_data[0].get_text()))
    print("24h Volume:\t{0}".format(coin_data[2].get_text()))
    print("Supply:\t{0}".format(coin_data[4].get_text()))

#Coingecko Funktionen

def _get_coingecko_top_coins()-> 'list':
    url = "https://www.coingecko.com/de"
    header = _loadJSON("header.json")
    req = requests.get(url, header)
    soup = BeautifulSoup(req.content, 'html.parser')

    #Current Value
    coins = soup.find_all("a", class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between")

    coin_list = []

    for coin in coins:
        coin_list.append(coin.get_text().lower().replace(" ", "-"))
    
    return coin_list

def _show_coin_data_coingecko(url, header)-> 'print':
    coin_name = url.split("/")
    print("Coin:\t{0}".format(coin_name[len(coin_name)-1]))

    req = requests.get(url, header)
    soup = BeautifulSoup(req.content, 'html.parser')

    coin_data = soup.find_all("span", class_="no-wrap")


    print("Current Value:\t{0}".format(coin_data[0].get_text()))
    print("MarketCap:\t{0}".format(coin_data[1].get_text()))
    print("24h Volume:\t{0}".format(coin_data[2].get_text()))