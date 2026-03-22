# Summative-Lab-Python-REST-API-with-Flask-Inventory-Management-System

Course 8 Summative Lab: Python REST API with Flask - Inventory Management System 


# 1. Set Up Instructions

Basic Installation:

Make sure Python and npm are installed
```python -V```
```pipenv install```
```npm install```

Start Backend Server:
```pipenv run python server/app.py```

Start Frontend UI:
```cd client```
```npm run dev```

# 2. API endpoints

* GET /inventory -> Fetch all items
* GET /inventory/item -> Fetch a single item by id
* POST /inventory -> Add a new item
* PUT /inventory/item -> Update an item
* DELETE /inventory/item -> Remove an item