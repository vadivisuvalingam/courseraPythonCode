import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty_list(self):
        """Test empty list."""
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_one_item_price_increase(self):
        """Test list of size one with just price increase."""
        actual = a1.stock_price_summary([0.02])
        expected = (0.02, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_one_item_price_decrease(self):
        """Test list of size one with just price decrease."""
        actual = a1.stock_price_summary([-0.02])
        expected = (0, -0.02)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_multiple_item_price_increase(self):
        """Test list of muliple numbers with just price increase."""
        actual = a1.stock_price_summary([0.01, 1.03, 0.05])
        expected = (1.09, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_multiple_item_price_decrease(self):
        """Test list of muliple numbers with just price decrease."""
        actual = a1.stock_price_summary([-0.01, -1.03, -0.05])
        expected = (0, -1.09)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_multiple_item_increase_first(self):
        """Test list of multiple numbers with both price increase
        and decrease, however with price increase order first and
        the price decrease last."""
        actual = a1.stock_price_summary([-0.01, -1.03, -0.05, 0.01, 1.03, 0.05])
        expected = (1.09, -1.09)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_multiple_item_decrease_first(self):
        """Test list of multiple numbers with both price increase
        and decrease, however with price decrease order first and
        the price increase last."""
        actual = a1.stock_price_summary([-0.01, -1.03, -0.05, 0.01, 1.03, 0.05])
        expected = (1.09, -1.09)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_list_multiple_item_no_order(self):
        """Test list of multiple numbers with both price increase
        and decrease with no particular order."""
        actual = a1.stock_price_summary([-0.01, 1.03, -0.05, 0.01, -1.03, 0.05])
        expected = (1.09, -1.09)
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
