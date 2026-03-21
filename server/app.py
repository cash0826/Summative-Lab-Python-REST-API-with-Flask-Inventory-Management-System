from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# separate data from presentation layer. Create a data access layer for reading and writing json -> providers

if __name__ == "__main__":
  app.run(port=5555, debug=True)
