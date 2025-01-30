from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from route.home import GetHomePage


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


api.add_resource(GetHomePage, '/api/')

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)
