#!/usr/bin/env python3
import ipdb

class CashRegister:
  items = []

  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    print("hello")
    

  def add_item(self, title, price, quantity=1):
    self.title = title
    self.price = price * quantity
    self.total = self.price + self.total
  
  def apply_discount(self):
    self.discount = (self.discount/100) * self.total
    self.total -= self.discount
    return f'After the discount, the total comes to ${int(self.total)}.'
    # ipdb.set_trace()

cash_register = CashRegister(20, 1000)  
print(cash_register.apply_discount())  