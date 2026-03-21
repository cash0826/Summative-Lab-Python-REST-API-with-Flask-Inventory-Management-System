# "id": 1,
# "name": "Product name 1",
# "description": "Description of product",
# "price": 1.99,
# "quantity": 10,
# "barcode": "0040987928",
# "category": "category",

from models.details import Details

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
    item =  cls(
      id = data.get('id', 0),
      name = data.get('name', ''),
      description = data.get('description', ''),
      price = data.get('price', 0),
      quantity = data.get('quantity', 0),
      barcode = data.get('barcode', ''),
      category = data.get('category', ''),
    )
    item.product_details = data.get("product_details", {})
    return item
    
  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "price" : self.price,
      "quantity": self.quantity,
      "barcode": self.barcode,
      "category": self.category,
      "product_details": self.product_details
    }