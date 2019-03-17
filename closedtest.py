import unittest
import identityfunc


# our teachers closed test here will run the id function created by the student to make sure we are getting the
# expected output

class ClosedTest(unittest.TestCase):

    def test_closed_test(self):
        result = identityfunc.id_func(6)
        self.assertEqual(result, (6,))

