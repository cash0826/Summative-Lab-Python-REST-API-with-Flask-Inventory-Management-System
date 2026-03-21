from abc import ABC, abstractmethod

class Product_Detail_Service(ABC):
  @abstractmethod
  def get_details_by_barcode():
    pass