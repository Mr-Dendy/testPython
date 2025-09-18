import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.add(8,7), 15)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(0,5), -5)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,0), 5)
  def test_sqrt(self):
    self.assertEqual(self.calculator.sqrt(-2), 3)
  def test_abs(self):
    self.assertEqual(self.calculator.abs(-3), 3)
  def test_pow(self):
    self.assertEqual(self.calculator.pow(2,3), 8)

if __name__ == "__main__":
  unittest.main()