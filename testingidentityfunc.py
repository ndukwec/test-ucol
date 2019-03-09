import unittest
import identityfunc


class TestingMethodsInOurProject(unittest.TestCase):

    # Our test method below will call our identity function to verify its output
    def test_method_to_verify_id_func_returns_a_tuple_with_passed_in_arguments(self):
        ret_value_from_id_func = identityfunc.id_func("hi there")
        self.assertEqual(ret_value_from_id_func, ("hi there",))


