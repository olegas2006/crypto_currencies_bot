import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import sys
import time

link = 'https://coinmarketcap.com/'

response = requests.get(link)




soup = BeautifulSoup(response.content,'html.parser')
bitcoin_data = soup.find('a', {'href': "/currencies/bitcoin/#markets"}).text
ethereum_data = soup.find('a', {'href': "/currencies/ethereum/#markets"}).text
tether_data = soup.find('a', {'href': "/currencies/tether/#markets"}).text
bnb_data = soup.find('a', {'href': "/currencies/bnb/#markets"}).text
xrp_data = soup.find('a', {'href': "/currencies/xrp/#markets"}).text
dogecoin_data = soup.find('a', {'href': "/currencies/dogecoin/#markets"}).text


print(response)
print(bitcoin_data)
print(ethereum_data)
print(tether_data)
print(bnb_data)
print(xrp_data)
print(dogecoin_data)

