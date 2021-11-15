'''
Interact with local PostgreSQL database using sql alchemy.
'''

import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import *
from menu_items import scrape_all
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
# For testing locally:
ip = '34.74.179.106'
DATABASEURI = "postgresql://postgres:jicc@{0}/postgres".format(ip)

engine = create_engine(DATABASEURI)


def populate_menu_items():
    menus = scrape_all()
    with engine.connect() as connection:
        for i in range(1, 4):
            dining_hall = menus[i-1]
            for key, val in dining_hall.items():
                connection.execute("INSERT INTO fooditem(foodName, imageURL, diningHall) \
                                    VALUES (%s, %s, %s) \
                                    ON CONFLICT (foodName) DO NOTHING", 
                                    key, val, i)

def getDiningHallMenuItems(diningHall):
    items=[]
    with engine.connect() as connection:
        cursor = connection.execute('SELECT* FROM foodItem where diningHall = %s', diningHall)
        for result in cursor:
            items.append(result)
        connection.close()
        return items
