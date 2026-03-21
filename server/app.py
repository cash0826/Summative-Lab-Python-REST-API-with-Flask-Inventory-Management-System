from flask import Flask, jsonify, request, abort
# from flask_cors import CORS
from providers.JSON_inventory_provider import JSON_Inventory_Provider
from models.inventory_item import Inventory_Item

app = Flask(__name__)
# CORS(app)

# separate data from presentation layer. Create a data access layer for reading and writing json -> providers

_provider = JSON_Inventory_Provider("data/inventory.json")

# Routes

## GET /inventory -> Fetch all items
@app.route("/inventory", methods=["GET"])
def get_all_inventory():
  _provider.load()
  inventory = _provider.all_inventory()
  return jsonify([item.to_dict() for item in inventory]), 200

## GET /inventory/<item> -> Fetch a single item by id
@app.route("/inventory/<int:id>", methods=["GET"])
def get_inventory_item(id):
  _provider.load()
  item = _provider.inventory_item_id(id)
  if not item:
    return jsonify({"error": "Item not found for requested id"}), 404
  return jsonify(item.to_dict()), 200

## POST /inventory -> Add a new item
@app.route("/inventory", methods=["POST"])
def create_new_item():
  if not request.json:
    abort(400, description="Missing JSON data")
    
  try:
    _provider.load()
    
    item = Inventory_Item.from_dict(request.json)
    new_item = _provider.add(item)
    if new_item:
      _provider.save()
      return jsonify(new_item), 201
    return "", 500
  except Exception as e:
    abort(500, description=e)
    
if __name__ == "__main__":
  app.run(port=5555, debug=True)
