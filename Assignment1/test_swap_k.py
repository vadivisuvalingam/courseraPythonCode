import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.

    def test_swap_k_empty_list(self):
        """Test that empty list with swaping zero items.."""
        actual = []
        k = 0
        expected = []
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_size_one_swap_zero(self):
        """Test list of size one with swaping zero items."""
        actual = ["a"]
        k = 0
        expected = ["a"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_even_size_swap_zero(self):
        """Test list of size two (even) with swaping zero items."""
        actual = ["a", "b"]
        k = 0
        expected = ["a", "b"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)        

    def test_swap_k_list_even_size_swap_one(self):
        """Test list of size two (even) with swaping one items."""
        actual = ["a", "b"]
        k = 1
        expected = ["b", "a"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_odd_size_swap_zero(self):
        """Test list of size three (odd) with swaping zero items."""
        actual = ["a", "b", "c"]
        k = 0
        expected = ["a", "b", "c"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_odd_size_swap_one(self):
        """Test list of size three (odd) with swaping one items."""
        actual = ["a", "b", "c"]
        k = 1
        expected = ["c", "b", "a"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_large_size_swap_zero(self):
        """Test list of size six (large) with swaping zero items."""
        actual = ["a", "b", "c", "d", "e", "f"]
        k = 0
        expected = ["a", "b", "c", "d", "e", "f"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_large_size_swap_one(self):
        """Test list of size six (large) with swaping one items."""
        actual = ["a", "b", "c", "d", "e", "f"]
        k = 1
        expected = ["f", "b", "c", "d", "e", "a"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)

    def test_swap_k_list_large_size_swap_two(self):
        """Test list of size six (large) with swaping two (multiple) items."""
        actual = ["a", "b", "c", "d", "e", "f"]
        k = 2
        expected = ["e", "f", "c", "d", "a", "b"]
        a1.swap_k(actual, k)
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
