import unittest
import sys
from datetime import datetime
from main_dining import check_open_halls


class Test_TestMainDining(unittest.TestCase):
    def test_john_jay_open(self):
        now = datetime.now()

        current_time = now.strftime('%H:%M:%S')
        day_of_week = now.weekday()

        dining_halls = check_open_halls()
        print(dining_halls)
        if day_of_week == 6 or (day_of_week >= 0 and day_of_week <= 4):
            if current_time >= '09:30:00' and current_time <= '21:00:00':
                assert 'John Jay Dining Hall' in dining_halls

    def test_ferris_open(self):
        now = datetime.now()

        current_time = now.strftime('%H:%M:%S')
        day_of_week = now.weekday()

        dining_halls = check_open_halls()
        if day_of_week >= 0 and day_of_week <= 4:
            if current_time >= '07:30:00' and current_time <= '20:00:00':
                assert 'Ferris Booth Commons' in dining_halls
        if day_of_week == 5:
            if current_time >= '09:00:00' and current_time <= '20:00:00':
                assert 'Ferris Booth Commons' in dining_halls

    def test_jjs_open(self):
        now = datetime.now()

        current_time = now.strftime('%H:%M:%S')
        day_of_week = now.weekday()

        dining_halls = check_open_halls()
        if day_of_week >= 0 and day_of_week <= 3:
            if current_time >= '12:00:00' and current_time <= '22:00:00':
                assert 'JJ\'s Place' in dining_halls
        if day_of_week >= 4 and day_of_week <= 5:
            if current_time >= '12:00:00' and current_time <= '00:00:00':
                assert 'JJ\'s Place' in dining_halls


if __name__ == '__main__':
    unittest.main()
