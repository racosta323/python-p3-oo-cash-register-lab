#!/usr/bin/env python3
import ipdb

class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    
    
  def add_item(self, title, price, quantity=1):
    updated_price = price * quantity
    self.total = updated_price + self.total
    number_of = quantity * title
    each_title = [each for each in number_of]
    ipdb.set_trace()
    return self.items.append(title * quantity)
    
    # return CashRegister.items
   
  def apply_discount(self):
    local_discount = (self.discount/100) * self.total
    self.total -= local_discount
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

new_register = CashRegister()
new_register.add_item("eggs", 1.99, 2)

# ipdb.set_trace()
