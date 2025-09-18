import math
class Calculator:

  def __init__(self):
    pass

  def add(self, x1, x2):
    return x1 + x2

  def multiply(self, x1, x2):
    return x1 * x2

  def subtract(self, x1, x2):
    return x1 - x2

  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2
      
  def sqrt(self, x):
    return math.sqrt(x)

  def abs(self, x):
    if x < 0:
        return x * (-1)
    return x
  def pow(self, x, rank):
    return x**rank
