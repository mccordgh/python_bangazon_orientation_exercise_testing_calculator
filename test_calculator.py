import unittest
from calculator import *

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):
    """Tests the four basic mathematical operations in calculator.py

    Methods:
     test_add(number, number)
     test_subtract(number, number)
     test_multiply(number, number)
     test_divide(number,number)
    """

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calc = Calculator()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(7, 2), 5)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(8, 2), 16)

  def test_divide(self):
    self.assertEqual(self.calc.divide(8, 2), 4)

if __name__ == '__main__':
    unittest.main()