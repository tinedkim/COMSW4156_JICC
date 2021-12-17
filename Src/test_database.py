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
        res += database.get_dining_hall_menu_items(2)
        res += database.get_dining_hall_menu_items(3)
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
        res += database.get_review_timestamps_for_dining_hall(2)
        res += database.get_review_timestamps_for_dining_hall(3)
        assert len(res) > 0

    def test_get_food_items(self):
        res = database.get_food_items()
        assert len(res) > 0

    def test_get_user_reviews(self):
        res = database.get_user_reviews('test')
        assert res != null

    def test_get_user_review_item_id(self):
        res = database.get_user_review_item_id('test')
        assert res != null

    def test_get_top_menu_items(self):
        res = database.get_top_menu_items()
        assert len(res) > 0

    def test_get_top_dining_halls(self):
        res = database.get_top_dining_halls()
        assert len(res) > 0

    def test_get_dining_hall_sign_ins(self):
        res = database.get_dining_hall_sign_ins()
        assert len(res) > 0
    
    def test_get_daily_sign_ins(self):
        res = database.get_daily_sign_ins()
        assert type(len(res)) is int

    def test_check_credentials(self):
        res = database.check_credentials('test', 'test@columbia.edu')
        assert res != -1
        res = database.check_credentials(1,2)
        assert res == -1
    
    def test_create_user(self):
        test_email = 'test@columbia.edu'
        res = database.create_user('test', 'test', test_email)
        assert res != -1
        res = database.create_user('test', 'test', test_email)
        assert res == -1

    def test_send_review(self):
        res = database.send_review('test', 'test', '1', '1', 'December 19, 2021')
        assert res != -1
        res = database.send_review(1,2,3,4,5)
        assert res == -1


if __name__ == '__main__':
    unittest.main()
