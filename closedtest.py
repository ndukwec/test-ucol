import unittest
import identityfunc


# our closed test (main method) here will run the id function to make sure we are getting the expected output

class ClosedTest(unittest.TestCase):

    def test_closed_test(self):
        result = identityfunc.id_func(6)
        self.assertEqual(result, (6,))

