from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

elements = [
    {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic number": 1,
        "atomic mass": 1.00794,
        "link": "http://www.chemicalelements.com/elements/h.html"
    },
    {
        "name": "Helium",
        "symbol": "He",
        "atomic number": 2,
        "atomic mass": 4.002602,
        "link": "http://www.chemicalelements.com/elements/he.html"
    }

]

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
