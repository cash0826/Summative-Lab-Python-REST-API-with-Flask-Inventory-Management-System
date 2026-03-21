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
def get_inventory():
  _provider.load()
  inventory = _provider.all_inventory()
  return jsonify([item.to_dict() for item in inventory]), 200

if __name__ == "__main__":
  app.run(port=5555, debug=True)
