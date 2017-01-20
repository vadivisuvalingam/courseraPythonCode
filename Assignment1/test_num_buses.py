import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_zero_people(self):
        """Test zero people case."""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_one_person(self):
        """Test one person case."""
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_one_full_bus(self):
        """Test one full bus."""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_one_full_bus_plus_one(self):
        """Test one full bus and one more person."""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)
        
    def test_num_buses_multiple_buses(self):
        """Test multiple buses."""
        actual = a1.num_buses(300)
        expected = 6
        self.assertEqual(expected, actual)        
        
if __name__ == '__main__':
    unittest.main(exit=False)
