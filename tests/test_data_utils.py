import unittest
from my_awesome_lib import data_utils

class TestDataUtils(unittest.TestCase):
    def test_flatten_list(self):
        self.assertEqual(data_utils.flatten_list([[1, 2], [3]]), [1, 2, 3])
        self.assertEqual(data_utils.flatten_list([]), [])

    def test_unique_elements(self):
        self.assertCountEqual(data_utils.unique_elements([1, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(data_utils.unique_elements([]), [])

    def test_chunk_list(self):
        self.assertEqual(data_utils.chunk_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(data_utils.chunk_list([], 3), [])
        with self.assertRaises(ValueError):
            data_utils.chunk_list([1, 2], 0)