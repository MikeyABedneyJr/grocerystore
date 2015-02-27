# This is a second take at making a store. The difference btwn this one and the next is
#   overall design.

# Are the details involving the STORE
class Store(object):
  def __init__(self, name):
    self.name = name

  # def Buy():
    # TODO: Add 

# This will be the CUSTOMER class

# This will be the CART that calculates the total

# This handles the INVENTORY
class Inventory(object):
  def __init__(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price

    def __str__(self):
      return self.name

# Make the starting inventory of items for the store
inventory_list = [
    Inventory("apple", 10, 1),
    Inventory("mop", 30, 3),
    Inventory("kashi", 20, 2)
    ]

pythonsrus = Store("PythonsRUs")


print inventory_list