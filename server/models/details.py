# "product_details": {
#   "brand": "product brands",
#   "product_name": "Product name again"

from dataclasses import dataclass, asdict

@dataclass
class Details():
  def __init__(self, brand='', product_name='', categories=''):
    self.brand = brand
    self.product_name = product_name
    self.categories = categories
  
  @classmethod
  def from_dict(cls, data):
    return cls(
      brand = data.get('brand', ''),
      product_name = data.get('product_name', ''),
      categories = data.get('categories', '')
    )
  
  def to_dict(self):
    return asdict(self)
