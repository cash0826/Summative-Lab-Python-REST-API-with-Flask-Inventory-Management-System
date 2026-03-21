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
    if not os.path.exists(self.filename):
      self._inventory = []
    with open(self.filename, "r", encoding="utf-8") as f:
      data = json.load(f)
      self._inventory = [ Inventory_Item.from_dict(item) for item in data]
  
  def save(self):
    data = [item.to_dict() for item in self.inventory]
    directory = os.path.dirname(self.file)
    