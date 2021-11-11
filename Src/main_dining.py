from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
from dotenv import load_dotenv
import os
import requests

dining_url = 'https://dining.columbia.edu/'

load_dotenv()
token = os.environ.get("scraping-token")
client = ScrapingAntClient(token=token)

content = client.general_request(dining_url).content
soup = BeautifulSoup(content, features='html5lib')
open_halls = []

dining_halls = soup.find('div', attrs={'class': 'col-xs-12 col-md-6'})
for hall in dining_halls.findAll('div', attrs={'class': 'location'}):
    spans = hall.findAll('span')
    hall_name = spans[0].text
    hall_status = spans[1].text
    if hall_status == 'Open':
        open_halls.append(hall_name)