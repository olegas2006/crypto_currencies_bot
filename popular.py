import requests
from bs4 import BeautifulSoup
from re import search
mass=[]
mass2 =[]
mass_links = []
popular_names = []
final_links = []
link = 'https://coinmarketcap.com/trending-cryptocurrencies/'
response = requests.get(link)
soup = BeautifulSoup(response.content,'html.parser')
popular1 = soup.find_all('a', {'class': "cmc-link"})
for i in range(len(popular1)):
    if search("/currencies/", str(popular1[i])):
        mass.append(popular1[i])
for i in range(len(mass)):
    st = str(mass[i])[38:]
    num = (st.find('/'))
    st = st[:num]
    if i%2 ==0:
        mass2.append(st)

for i in range(len(mass2)):
    mass_links.append("https://coinmarketcap.com/currencies/"+mass2[i]+"/")

for i in range(len(mass2)):
    print(mass2[i])
for i in range(len(mass2)):
    print(mass_links[i])
popular_names = mass2
final_links =mass_links