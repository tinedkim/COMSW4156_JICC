import unittest
import menu_items

class Test_TestMenuItems(unittest.TestCase):

    def test_scrape_all(self):
        menus = menu_items.scrape_all(True)