import os
import json

# JSON Data provider: initialize empty file, load data, save data. Load and Save are primary functions for a file.
# Then we got all other methods: get all, get by id, add, update and delete. These methods will be called with the routes
# This data provider is responsible for all the data persistance. It does not include validation logic

from models.inventory_item import Inventory_Item

class JSON_Inventory_Provider():
  def __init__(self, filename):
    self.filename = filename
    self._inventory = []
    
  def load(self):
    if os.path.exists(self.filename):
      with open(self.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        self._inventory = [ Inventory_Item.from_dict(item) for item in data]
    else:
      self._inventory = []
  
  def save(self):
    data = [item.to_dict() for item in self._inventory]
    with open(self.filename, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2)
  
  def all_inventory(self):
    return self._inventory
  
  def inventory_item_id(self, id):
    return next((item for item in self._inventory if item.id == id), None)
  
  def add_item(self, item):
    if item.id is None:
      max_id = max([i.id for i in self._inventory]) if self._inventory else 0
      item.id = max_id + 1
      
    self._inventory.append(item)
    return item
  
  def update(self, id: int, item: Inventory_Item):
    for i, existing_item in enumerate(self._inventory):
      if existing_item.id == id:
        self._inventory[i] = item
        return item
    return None
  
  def delete(self, id:int):
    initial_len = len(self._inventory)
    self._inventory = [i for i in self._inventory if i.id != id]
    return len(self._inventory) < initial_len
  
  def lookup(self, barcode):
    pass