from flask import Flask, jsonify, request, current_app, abort, g, make_response
# from flask_cors import CORS
from providers.JSON_inventory_provider import JSON_Inventory_Provider
from models.inventory_item import Inventory_Item
from services.open_food_facts_service import Open_Food_Facts_Service
import os

app = Flask("Inventory Management System") 

@app.before_request
def app_path():
  g.path = os.path.abspath(os.getcwd()) # can be used for additional checks like authentication, prior to loading page
  
@app.route("/")
def home():
  host = request.headers.get("Host")
  appname = current_app.name
  response_body = f'''
  <h1> {appname} </h1>
  <h2> {host} </h2>
  <h3> {g.path} </h3>
  <p> API endpoint: /inventory </p>
  '''
  status_code = 200
  headers = {}
  return make_response(response_body, status_code, headers)
  
# Notes: Separate data from presentation layer. 
# Create a data access layer for reading and writing json -> providers

_provider = JSON_Inventory_Provider("data/inventory.json")
detail_services = Open_Food_Facts_Service("https://world.openfoodfacts.net/api/v2/product/{barcode}.json")

# Routes

## GET /inventory -> Fetch all items
@app.route("/inventory", methods=["GET"])
def get_all_inventory():
  barcode = request.args.get("barcode")
  _provider.load() 
  inventory = _provider.all_inventory()
  if barcode:
    inventory = [item for item in inventory if item.barcode == barcode]
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
    new_item = _provider.add_item(item)
    if new_item:
      _provider.save()
      return jsonify(new_item.to_dict()), 201
    return "", 500
  except Exception as e:
    abort(500, description=e)
    
## PUT /inventory/<item> -> Update an item
@app.route("/inventory/<int:id>", methods=["PUT"])
def update_item(id):
  if not request.json:
    abort(400, description="Missing JSON data")
  try:
    _provider.load()
    item = Inventory_Item.from_dict(request.json)
    updated_item = _provider.update(id, item)
    if updated_item:
      _provider.save()
      return jsonify(updated_item.to_dict()), 200 # Returns updated item
    abort(400, description=f"Item with id {id} in inventory not found")
  except Exception as e:
    abort(400, description=str(e))
    
## DELETE /inventory/<item> -> Remove an item
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
  _provider.load()
  success = _provider.delete(id)
  if success:
    _provider.save()
    return jsonify({"message": f"Deleted Item with id {id}"}), 204
  abort(404, description="Inventory Item with id {id} not found")

if __name__ == "__main__":
  app.run(port=5555, debug=True)
