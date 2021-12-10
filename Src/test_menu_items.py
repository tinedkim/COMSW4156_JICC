import unittest
import menu_items


class Test_TestMenuItems(unittest.TestCase):

    def test_scrape_all(self):
        menus = menu_items.scrape_all(True)

        # We will check if two random items
        # of each dining hall are the same

        # Ferris
        assert "Turkey Sausage" in menus[0].keys()
        test_url = menus[0]["Turkey Sausage"]
        actual_url = 'url(/sites/default/files/2019-08/turkey%20sausage.jpg)'
        self.assertEqual(test_url, actual_url)

        assert "Greek Chicken Orzo Soup" in menus[0].keys()
        test_url = menus[0]["Greek Chicken Orzo Soup"]
        actual_url =\
            'url(/sites/default/files/2019-06/greekorzochickensoup.jpg)'
        self.assertEqual(test_url, actual_url)

        # John Jay
        assert "Roasted Vegetables" in menus[1].keys()
        test_url = menus[1]["Roasted Vegetables"]
        actual_url =\
            'url(/sites/default/files/2019-06/roasted_vegetables.jpg)'
        self.assertEqual(test_url, actual_url)

        assert "Whole Wheat Penne" in menus[1].keys()
        test_url = menus[1]["Whole Wheat Penne"]
        actual_url =\
            'url(/sites/default/files/2019-06/whole_wheat_penne_cooked_and_uncooked.jpg)'
        self.assertEqual(test_url, actual_url)

        # JJ's
        assert "JJ's Oreo Stuffed French Toast" in menus[2].keys()
        test_url = menus[2]["JJ's Oreo Stuffed French Toast"]
        actual_url =\
            'url(/sites/default/files/2019-07/frenchtoast.JJs_.everyday.jpg)'
        self.assertEqual(test_url, actual_url)

        assert "JJ's Truffle Mushroom Grilled Cheese" in menus[2].keys()
        test_url = menus[2]["JJ's Truffle Mushroom Grilled Cheese"]
        actual_url = 'url(/sites/default/files/2019-06/grilled_cheese_3_0.jpg)'
        self.assertEqual(test_url, actual_url)


if __name__ == '__main__':
    unittest.main()
