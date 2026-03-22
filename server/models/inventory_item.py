
class Inventory_Item():
  def __init__(self, id=None, name='', description='', price=0.0, quantity=0, barcode='', category='', product_details=None):
    self.id = id
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
    self.barcode = barcode
    self.category = category
    self.product_details = product_details or {}
  
  @classmethod
  def from_dict(cls, data):
    item =  cls(
      id = data.get('id', None),
      name = data.get('name') or '',
      description = data.get('description') or '',
      price = data.get('price', 0),
      quantity = data.get('quantity', 0),
      barcode = data.get('barcode') or '',
      category = data.get('category') or '',
    )
    item.product_details = data.get("product_details") or {}
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