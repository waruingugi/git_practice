import unittest


# The function we want to test
def times_ten(number):
    return number * 100


# Our test class
class TestTimesTen(unittest.TestCase):
    
    # A test method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest(num):
                expected_result = num * 10
                message = f'Expected times_ten({num}) to return {expected_result}'

                self.assertEqual(times_ten(num), expected_result, message)

unittest.main()
