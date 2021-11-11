import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import *
from menu_items import scrape_all

load_dotenv()

DATABASEURI = os.environ.get("database-uri")

engine = create_engine(DATABASEURI, connect_args={'connect_timeout': 10})


def populate_menu_items():
    menus = scrape_all()
    with engine.connect() as connection:
        for i in range(1, 4):
            dining_hall = menus[i]
            for key, val in dining_hall.items():
                connection.execute("INSERT INTO foodItem(foodName, imageURL, \
                                   diningHall) VALUES (%s, %s, %d)",
                                   key, val, dining_hall)
