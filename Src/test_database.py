from sqlalchemy import *
import unittest
import database
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
# For testing locally:
ip = '34.74.179.106:5432'
ip = 'localhost'
DATABASEURI = "postgresql://postgres:jicc@{0}/postgres".format(ip)

engine = create_engine(DATABASEURI)

class Test_TestDatabase(unittest.TestCase):

    def test_populate_menu_items(self):
        database.populate_menu_items()

        # Check if database is not empty
        with engine.connect() as connection:
            cursor = connection.execute("SELECT D.id FROM diningHall D")
            for hall in cursor:
                id = hall[0]
                item_counts = connection.execute("SELECT COUNT(*) FROM foodItem F\
                                            WHERE F.diningHall = {0}".format(id))
                for count in item_counts:
                    num_entry = count[0]
                    print(num_entry, "for id: ", id)
                    self.assertTrue(num_entry > 0)

    def test_dining_hall_menu_items(self):
        res = database.getDiningHallMenuItems(1)
        assert len(res) > 0

    def test_dining_halls(self):
        res = database.getDiningHalls()
        assert len(res) > 0

    def test_get_food_reviews(self):
        res = database.getReviewsForFoodItem(2)
        assert len(res) > 0
        res = database.getReviewsForFoodItem(-1)
        assert len(res) == 0

    def test_get_timestamps_for_dining_hall(self):
        res = database.getReviewTimestampsForDiningHall(1)
        assert len(res) > 0

    def test_get_food_items(self):
        res = database.getFoodItems()
        assert len(res) > 0



if __name__ == '__main__':
    unittest.main()
