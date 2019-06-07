from flask import Flask
from flask_restful import Api, Resource, reqparse
from elements import all_elements

app = Flask(__name__)
api = Api(app)
SERVER_ADDR = "167.99.4.38"
elements = all_elements

class Element(Resource):
    def get(self, symbol):
        for e in elements:
            if(symbol == e["symbol"]):
                return e, 200
        return "Element not found", 404

class All(Resource):
    def get(self):
        return elements

api.add_resource(Element, "/elements/<string:symbol>")
api.add_resource(All, "/")

if __name__ == "__main__":
    app.debug = True
    app.run()
