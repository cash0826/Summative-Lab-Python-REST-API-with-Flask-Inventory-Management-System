# "id": 1,
# "name": "Product name 1",
# "description": "Description of product",
# "price": 1.99,
# "quantity": 10,
# "barcode": "0040987928",
# "category": "category",

from dataclasses import dataclass, asdict
import Details

class Inventory_Item():
  def __init__(self, id=None, name='', description='', price=0.0, quantity=0, barcode='', category='', product_details={}):
    self.id = id
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
    self.barcode = barcode
    self.category = category
    self.product_details = {}
  
  @classmethod
  def from_dict(cls, data):
    return cls(
      id = data.get('id', 0),
      name = data.get('name', ''),
      description = data.get('description', ''),
      price = data.get('price', 0),
      quantity = data.get('quantity', 0),
      barcode = data.get('barcode', ''),
      category = data.get('category', ''),
      product_details = [Details.from_dict(d) for d in data.get('product_details', {})]
    )
    
  def to_dict(self):
    return asdict()