from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
import requests


dining_url = 'https://dining.columbia.edu/'

client = ScrapingAntClient(token='8a2062388f4f4cba84269e04c380cd10')

content= client.general_request(dining_url).content
soup = BeautifulSoup(content, features='html5lib')
open_halls = []

dining_halls = soup.find('div', attrs = {'class': 'col-xs-12 col-md-6'})
for hall in dining_halls.findAll('div', attrs = {'class': 'location'}):
    spans = hall.findAll('span')
    hall_name = spans[0].text
    hall_status = spans[1].text
    if hall_status == 'Open':
        open_halls.append(hall_name)