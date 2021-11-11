from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get("scraping-token")
client = ScrapingAntClient(token=token)

ferris_url = 'https://dining.columbia.edu/content/ferris-booth-commons-0'
john_jay_url = 'https://dining.columbia.edu/content/john-jay-dining-hall'
jjs_url = 'https://dining.columbia.edu/content/jjs-place-0'


def scrape_all():
    urls = [ferris_url, john_jay_url, jjs_url]
    menus = [{}, {}, {}]

    # Each dining hall has a menu dictionary associating food item to image url
    for url, menu in zip(urls, menus):
        content = client.general_request(url).content
        soup = BeautifulSoup(content, features='html5lib')

        food_items = soup.find('div', attrs={'class': 'cu-dining-meals'})
        for item in food_items.findAll('div', attrs={'class': 'meal-content'}):
            food_name = item.find('h5').text
            image_style = item.find('div', attrs={'class': 'image bg animated'})["style"]
            img_url = image_style.split(' ')[-1]
            menu.update({food_name: img_url})

    return menus


def scrape_hall(dining_hall_url):
    menu = {}

    content = client.general_request(dining_hall_url).content
    soup = BeautifulSoup(content, features='html5lib')

    food_items = soup.find('div', attrs={'class': 'cu-dining-meals'})
    for item in food_items.findAll('div', attrs={'class': 'meal-content'}):
        food_name = item.find('h5').text
        image_style = item.find('div', attrs={'class': 'image bg animated'})["style"]
        img_url = image_style.split(' ')[-1]
        menu.update({food_name: img_url})

    return menu
