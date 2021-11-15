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

def get_content(idx, testing = False):
    urls = [ferris_url, john_jay_url, jjs_url]
    html = ['../testing/ferris.html', '../testing/johnjay.html', '../testing/jjs.html']

    if testing:
        html_file = open(html[idx], "r")
        content = html_file.read()
        html_file.close()
    else:
        content = client.general_request(urls[idx]).content

    return content


def scrape_all(testing = False):
    menus = [{}, {}, {}]

    # Each dining hall has a menu dictionary associating food item to image url
    for i, menu in zip(range(3), menus):
        content = get_content(i, testing)
        soup = BeautifulSoup(content, features='html5lib')

        food_items = soup.find('div', attrs={'class': 'cu-dining-meals'})
        for item in food_items.findAll('div', attrs={'class': 'meal-content'}):
            food_name = item.find('h5').text
            image_style = item.find('div',
                                    attrs={'class':
                                           'image bg animated'})["style"]
            img_url = image_style.split(' ')[-1]
            menu.update({food_name: img_url})

    return menus
