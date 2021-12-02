'''
Interact with local PostgreSQL database using sql alchemy.
'''

import os
from dotenv import load_dotenv
from sqlalchemy import *
from menu_items import scrape_all
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
# For testing locally:
ip='35.237.182.227'
DATABASEURI = "postgresql://postgres:jicc@{0}/postgres".format(ip)

engine = create_engine(DATABASEURI)


def executeQuery(query, values=None, returnResults=True):
    with engine.connect() as connection:
        cursor = connection.execute(query) if values is None\
            else connection.execute(query, values)
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
                connection.execute("INSERT INTO fooditem\
                                    (foodName, imageURL, diningHall)\
                                    VALUES (%s, %s, %s)\
                                    ON CONFLICT (foodName) DO NOTHING",
                                   key, val, i)


def getRows(cur):
    return [dict(result) for result in cur]


def getDiningHallMenuItems(diningHall):
    return getRows(executeQuery('SELECT* FROM foodItem\
                                 where diningHall = %s', diningHall))


def getDiningHalls():
    return getRows(executeQuery('SELECT * FROM diningHall'))


def getReviewsForFoodItem(foodItemId):
    return getRows(executeQuery('SELECT * FROM REVIEW\
                                 where foodItemId = %s', foodItemId))


def getReviewTimestampsForDiningHall(diningHall):
    return getRows(executeQuery('SELECT date FROM REVIEW\
                                 inner join foodItem on\
                                 foodItem.foodItemID = review.foodItemId\
                                 WHERE foodItem.diningHall = %s', diningHall))


def getFoodItems():
    return getRows(executeQuery('SELECT * from foodItem'))


def checkCredentials(name, email):
    return getRows(executeQuery('SELECT uni FROM\
                                 person WHERE name = %s\
                                 and email = %s', name, email))


def createUser(name, uni, email):
    try: 
        executeQuery('INSERT INTO\
                      person(name, uni, email)\
                      VALUES(%s, %s, %s)', name, uni, email )
        return 1
    except:
        return -1


def getUserReviews(uni):
    return getRows(executeQuery('SELECT text, rating\
                                 FROM review where\
                                 uni = %s', uni))

def getUserReviewItemid(uni):
    return getRows(executeQuery('SELECT fooditemid\
                                 FROM review where\
                                 uni = %s', uni))

def sendReview(uni, review, rating, foodItem):
    try:
        executeQuery('INSERT INTO review(text, rating, uni, fooditemid)\
                      VALUES(%s, %s, %s, %s)', review, rating, uni, foodItem )
        return 1
    except:
        return -1
