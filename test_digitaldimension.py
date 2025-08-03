# test_digitaldimension.py
"""
Tests for DigitalDimension module.
"""

import unittest
from digitaldimension import DigitalDimension

class TestDigitalDimension(unittest.TestCase):
    """Test cases for DigitalDimension class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalDimension()
        self.assertIsInstance(instance, DigitalDimension)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalDimension()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
