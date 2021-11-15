import unittest
import database
class TestStringMethods(unittest.TestCase):

    def testDiningHallMenuItems():
        res = database.getDiningHallMenuItems(1)
        assert len(res) > 0
if __name__ == '__main__':
    unittest.main()
