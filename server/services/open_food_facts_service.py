import requests
from services.product_details_service import Product_Detail_Service

class Open_Food_Facts_Service(Product_Detail_Service):
  def __init__(self, url_template):
    self.url_template = url_template
    
  def get_details_by_barcode(self, barcode):
    if not barcode:
      return {}
    
    url = self.url_template.format(barcode=barcode)
    try:
      response = requests.get(url, timeout=5)
      response.raise_for_status()
      data = response.json()
      
      if data.get("status") == 1:
        product = data.get("product", {})
        product_details = {
          "product_name": product.get("product_name"),
          "brands": product.get("brands"),
          "categories": product.get("categories")
        }
        return product_details
      
    except Exception as e:
      print(f"Error fetching data from OpenFoodFacts: {e}")
      
    return {}
  
# test = Open_Food_Facts_Service("https://world.openfoodfacts.net/api/v2/product/{barcode}.json")
# print(test.get_details_by_barcode('4008713702750'))