from flask import Flask, jsonify
# from flask_cors import CORS
from providers.JSON_inventory_provider import JSON_Inventory_Provider

app = Flask(__name__)
# CORS(app)

# separate data from presentation layer. Create a data access layer for reading and writing json -> providers

_provider = JSON_Inventory_Provider("data/inventory.json")

# Routes

## GET /inventory
@app.route("/inventory", methods=["GET"])
def get_all_inventory():
  _provider.load()
  inventory = _provider.all_inventory()
  return jsonify([item.to_dict() for item in inventory]), 200

## GET /inventory/<item>
@app.route("/inventory/<int:id>", methods=["GET"])
def get_inventory_item(id):
  _provider.load()
  item = _provider.inventory_item_id(id)
  if not item:
    return jsonify({"error": "Item not found for requested id"}), 404
  return jsonify(item.to_dict()), 200

if __name__ == "__main__":
  app.run(port=5555, debug=True)
