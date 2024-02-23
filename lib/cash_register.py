#!/usr/bin/env python3
import ipdb

class CashRegister:
  
  prices = []

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    
  def add_item(self, title, price, quantity=1):
    updated_price = price * quantity
    self.total = updated_price + self.total
    number_of_titles = [self.items.append(title) for n in range(quantity)]
    CashRegister.prices.append(updated_price)
    return CashRegister.prices
    
    
  def apply_discount(self):
    local_discount = (self.discount/100) * self.total
    self.total -= local_discount
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= CashRegister.prices[-1]