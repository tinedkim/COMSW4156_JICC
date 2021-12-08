'''
Interact with local PostgreSQL database using sql alchemy.
'''

import os
from dotenv import load_dotenv
from sqlalchemy import *
from menu_items import scrape_all
from requests import get

load_dotenv("./env")

ip = get('https://api.ipify.org').content.decode('utf8')
# For testing locally:
ip = os.environ.get("ip")
DATABASEURI = "postgresql://postgres:jicc@{0}/postgres".format(ip)

engine = create_engine(DATABASEURI)

def execute_query(query, values = None, returnResults = True):
    with engine.connect() as connection:
        cursor = connection.execute(query) if values is None else connection.execute(query, values)
        results = None
        if returnResults:
            results = cursor.fetchall()
        connection.close()
        return results

def populate_menu_items():
    menus = scrape_all()
    print('scraping completed')
    with engine.connect() as connection:
        for i in range(1, 4):
            dining_hall = menus[i-1]
            for key, val in dining_hall.items():
                connection.execute("INSERT INTO fooditem(foodName, imageURL, diningHall) \
                                    VALUES (%s, %s, %s) \
                                    ON CONFLICT (foodName) DO NOTHING", 
                                    key, val, i)

def get_rows(cur):
    return [dict(result) for result in cur]

def get_dining_hall_menu_items(diningHall):
    return get_rows(execute_query('SELECT* FROM foodItem where diningHall = %s', diningHall))
    
def get_dining_halls():
    return get_rows(execute_query('SELECT * FROM diningHall'))

def get_reviews_for_food_item(foodItemId):
    return get_rows(execute_query('SELECT * FROM REVIEW where foodItemId = %s', foodItemId))

def get_review_timestamps_for_dining_hall(diningHall):
    return get_rows(execute_query('SELECT date FROM REVIEW inner join foodItem on foodItem.foodItemID = review.foodItemId WHERE foodItem.diningHall = %s', diningHall))

def get_food_items():
    return get_rows(execute_query('SELECT * from foodItem'))
