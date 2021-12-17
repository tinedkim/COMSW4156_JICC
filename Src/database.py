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
ip = os.environ.get("ip") or "localhost"
DATABASEURI = "postgresql://postgres:jicc@{0}/postgres".format(ip)

engine = create_engine(DATABASEURI)

def execute_query(query, values = None, returnResults = True):
    with engine.connect() as connection:
        cursor = connection.execute(query) if values is None\
            else connection.execute(query, *values)
        results = None
        if returnResults:
            results = cursor.fetchall()
        connection.close()
        return results


def populate_menu_items(testing=False):
    menus = scrape_all(testing)
    print('scraping completed')
    with engine.connect() as connection:
        for i in range(1, 4):
            dining_hall = menus[i-1]
            for key, val in dining_hall.items():
                print(f'insert {key} {val} for {i}') 
                connection.execute("INSERT INTO fooditem\
                                    (foodName, imageURL, diningHall)\
                                    VALUES (%s, %s, %s)\
                                    ON CONFLICT (foodName) DO NOTHING",
                                   key, val, i)


def get_rows(cur):
    return [dict(result) for result in cur]


def get_dining_hall_menu_items(diningHall):
    return get_rows(execute_query('SELECT* FROM foodItem where diningHall = %s', [diningHall]))
    

def get_dining_halls():
    return get_rows(execute_query('SELECT * FROM diningHall'))


def get_reviews_for_food_item(foodItemId):
    return get_rows(execute_query('SELECT * FROM REVIEW where foodItemId = %s', [foodItemId]))


def get_review_timestamps_for_dining_hall(diningHall):
    return get_rows(execute_query('SELECT date FROM REVIEW inner join foodItem on foodItem.foodItemID = review.foodItemId WHERE foodItem.diningHall = %s', [diningHall]))


def get_food_items():
    return get_rows(execute_query('SELECT * from foodItem'))


def check_credentials(name, email):
    try: 
        return get_rows(execute_query('SELECT uni FROM\
                                  person WHERE name = %s\
                                  and email = %s', [name, email]))
    except:
        return -1


def create_user(name, uni, email):
    try: 
        execute_query('INSERT INTO\
                      person(name, uni, email)\
                      VALUES(%s, %s, %s)', [name, uni, email], returnResults=False)
        return 1
    except:
        return -1


def get_user_reviews(uni):
    return get_rows(execute_query('SELECT text, rating\
                                 FROM review where\
                                 uni = %s', [uni]))


def get_user_review_item_id(uni):
    return get_rows(execute_query('SELECT R.fooditemid, F.foodname, F.imageurl\
                                 FROM review R, foodItem F  where\
                                 uni = %s AND F.fooditemid = R.fooditemid', [uni]))


def send_review(uni, review, rating, foodItem, date):
    try:
        execute_query('INSERT INTO review(text, rating, uni, fooditemid, date)\
                      VALUES(%s, %s, %s, %s, %s)', [review, rating, uni, foodItem, date], returnResults=False )
        return 1
    except:
        return -1


def get_top_menu_items():
    return get_rows(execute_query('SELECT foodname, avg(rating) as avg_rating\
                                 FROM review inner join fooditem on\
                                 fooditem.fooditemid = review.fooditemid\
                                 GROUP by fooditem.fooditemid\
                                 ORDER by avg_rating desc\
                                 FETCH FIRST 10 ROWS ONLY'))


def get_top_dining_halls():
    return get_rows(execute_query('SELECT name, avg(rating) as avg_rating\
                                 FROM review left join fooditem\
                                 on review.fooditemid = fooditem.fooditemid\
                                 left join dininghall on dininghall.id = fooditem.dininghall\
                                 GROUP by name\
                                 ORDER by avg_rating desc'))


def get_dining_hall_sign_ins():
    return get_rows(execute_query('SELECT name, count(name)\
                                 FROM review left join fooditem\
                                 on review.fooditemid = fooditem.fooditemid\
                                 left join dininghall on dininghall.id = fooditem.dininghall\
                                 GROUP by name'))


def get_daily_sign_ins():
    return get_rows(execute_query("SELECT name, count(name)\
                                 FROM review left join fooditem\
                                 on review.fooditemid = fooditem.fooditemid\
                                 left join dininghall on dininghall.id = fooditem.dininghall\
                                 where review.date >= CURRENT_DATE - INTERVAL '1 DAY'\
                                 GROUP by name"))