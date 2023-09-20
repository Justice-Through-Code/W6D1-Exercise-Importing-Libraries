import unittest
import pylint
import datetime
import statistics
import math
import random


# Function to count comments in a Python script
def count_comments(script_filename):
    with open(script_filename, 'r') as script_file:
        lines = script_file.readlines()
    comment_count = sum(1 for line in lines if line.strip().startswith('#'))
    return comment_count

class TestImportLibraryExercise(unittest.TestCase):
    def test_datetime(self):
        # Test the datetime function
        current_datetime = datetime.datetime.now()
        self.assertIsInstance(current_datetime, datetime.datetime)

    def test_statistics(self):
        # Test the statistics function
        numbers = [10, 20, 30, 40, 50]
        mean = statistics.mean(numbers)
        self.assertEqual(mean, 30.0)  # Assuming the mean of these numbers is 30.0

    def test_math(self):
        # Test the math function
        number = 25
        square_root = math.sqrt(number)
        self.assertEqual(square_root, 5.0)  # Assuming the square root is 5.0

    def test_random(self):
        # Test the random function
        random_number = random.randint(1, 100)
        self.assertTrue(1 <= random_number <= 100)  # Assuming it's within the specified range

    def test_comment_count(self):
        # Test that there are at least 4 comments in the script
        script_filename = 'import_library.py'
        comment_count = count_comments(script_filename)
        self.assertGreaterEqual(comment_count, 4)

if __name__ == '__main__':
    unittest.main()
