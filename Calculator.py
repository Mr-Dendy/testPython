import math
class Calculator:

  def __init__(self):
    pass

  def add(self, x1, x2):
    if type(x1) != int or type(x2) != int:
      raise ValueError("Не соответствие типа!")
    return x1 + x2

  def multiply(self, x1, x2):
    if type(x1) != int or type(x2) != int:
      raise ValueError("Не соответствие типа!")
    return x1 * x2

  def subtract(self, x1, x2):
    if type(x1) != int or type(x2) != int:
      raise ValueError("Не соответствие типа!")
    return x1 - x2
  def divide(self, x1, x2):
    if x2 == 0:
      raise ValueError("x2 равен 0")
    elif type(x1) != int or type(x2) != int:
      raise ValueError("Не соответствие типа!")
    return x1 / x2
      
  def sqrt(self, x):
    if x < 0:
      raise ValueError("Корень не может содержать отрицательное число!")
    if type(x) != int:
      raise ValueError("Не соответствие типа!")
    return math.sqrt(x)

  def abs(self, x):
    if type(x) != int:
      raise ValueError("Не соответствие типа!")
    if x < 0:
      return x * (-1)
    return x

  def pow(self, x, rank):
    if type(x) != int or type(rank) != int:
      raise ValueError("Не соответствие типа!")
    return x**rank