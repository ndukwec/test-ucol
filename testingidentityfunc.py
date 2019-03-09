import unittest
import identityfunc


class TestingMethodsInOurProject(unittest.TestCase):

    # Our test method below will call our identity function to verify its output
    def test_method_to_verify_id_func_returns_a_type_of_tuple(self):
        ret_value_from_idfunc = identityfunc.id_func("hi there")
        self.assertEqual(ret_value_from_idfunc, ("hi there",))


