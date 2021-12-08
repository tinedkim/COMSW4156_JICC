from sqlalchemy import *
import unittest
import database
from requests import get

class Test_TestDatabase(unittest.TestCase):
    '''
    def test_populate_menu_items(self):
        database.populate_menu_items()

        # Check if database is not empty
        with engine.connect() as connection:
            cursor = connection.execute("SELECT D.id FROM diningHall D")
            for hall in cursor:
                id = hall[0]
                item_counts = connection.execute("SELECT COUNT(*)\
                                                  FROM foodItem F\
                                                  WHERE F.diningHall\
                                                  = {0}".format(id))
                for count in item_counts:
                    num_entry = count[0]
                    print(num_entry, "for id: ", id)
                    self.assertTrue(num_entry > 0)
    '''
    def test_dining_hall_menu_items(self):
        res = database.get_dining_hall_menu_items(1)
        assert len(res) > 0

    def test_dining_halls(self):
        res = database.get_dining_halls()
        assert len(res) > 0

    def test_get_food_reviews(self):
        res = database.get_reviews_for_food_item(2)
        assert len(res) > 0
        res = database.get_reviews_for_food_item(-1)
        assert len(res) == 0

    def test_get_timestamps_for_dining_hall(self):
        res = database.get_review_timestamps_for_dining_hall(1)
        assert len(res) > 0

    def test_get_food_items(self):
        res = database.get_food_items()
        assert len(res) > 0

if __name__ == '__main__':
    unittest.main()
