import unittest

from utils.arrs import get
#my_slice

class TestGet(unittest.TestCase):
    def test_get_existing_index(self):
        self.assertEqual(get([1, 2, 3], 1), 2)

    def test_get_non_existing_index(self):
        self.assertEqual(get([1, 2, 3, 4], -4), None)

    def test_get_negative_index(self):
        self.assertEqual(get([1, 2, 3], -1), None)

    def test_get_default_value(self):
        self.assertEqual(get([1, 2, 3], -3, "default"), "default")


# class TestGet(unittest.TestCase):
#     def test_get_existing_key(self):
#         my_dict = {1: -1, 2: -2, 3: -3}
#         self.assertEqual(get(my_dict, 2), -2)
#
#     def test_get_nonexisting_key(self):
#         my_dict = {1: -1, 2: 2, 3: 3}
#         self.assertIsNone(get(my_dict, -1))
#
#     def test_get_nonexisting_key_with_default(self):
#         my_dict = {1: 1, 2: -2, 3: 3}
#         self.assertEqual(get(my_dict, -2, default=0), 0)
#
#     def test_get_nested_key(self):
#         my_dict = {1: {2: {3: 3}}}
#         self.assertEqual(get(my_dict, -1.-2.-3), None)
#
#     def test_get_nested_key_nonexisting(self):
#         my_dict = {1: {2: {3: 3}}}
#         self.assertIsNone(get(my_dict, -1.-2.-3))


# class TestMySlice(unittest.TestCase):
#     def test_my_slice_full(self):
#         self.assertEqual(my_slice([-1, 2, 3]), [-1, 2, 3])
#
#     def test_my_slice_start(self):
#         self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
#
#     def test_my_slice_end(self):
#         self.assertEqual(my_slice([1, 2, 3], end=2), [1, 2])
#
#     def test_my_slice_start_and_end(self):
#         self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
#
#     def test_my_slice_empty(self):
#         self.assertEqual(my_slice([]), [])
#
#     def test_my_slice_negative_start(self):
#         self.assertEqual(my_slice([1, 2, 3], -2), [2, 3])
#
#     def test_my_slice_negative_end(self):
#         self.assertEqual(my_slice([1, 2, 3], end=-1), [1, 2])
#
#     def test_my_slice_negative_start_and_end(self):
#         self.assertEqual(my_slice([1, 2, 3], -2, -1), [2])

#
# if __name__ == '__main__':
#     unittest.main()