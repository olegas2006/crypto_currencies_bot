import requests
from bs4 import BeautifulSoup
from re import search
mass=[]
mass2 =[]
mass_links = []
popular_names = []
final_links = []
link = 'https://coinmarketcap.com/new/'
response = requests.get(link)
soup = BeautifulSoup(response.content,'html.parser')
popular1 = soup.find_all('a', {'class': "cmc-link"})
for i in range(len(popular1)):
    if search("/currencies/", str(popular1[i])):
        mass.append(popular1[i])
mass =mass[::]
for i in range(len(mass)):
    st = str(mass[i])
    mass2.append(st[26::])
for i in range(len(mass2)):
    st = str(mass2[i])
    num = (st.find('/', 12))
    mass_links.append((st[:num+1]))


link = 'https://coinmarketcap.com/new/'
response = requests.get(link)
soup = BeautifulSoup(response.content,'html.parser')
popular_names1 = soup.find_all('p', {'class': "sc-e225a64a-0 ePTNty"})
for i in range (len(popular_names1)):
    popular_names.append(popular_names1[i].text)
for i in range(len(mass_links)):
    final_links.append('https://coinmarketcap.com'+mass_links[i])
for i in range(len(popular_names)):
    print(popular_names[i]+ "   "+ final_links[i])
print(len(mass))