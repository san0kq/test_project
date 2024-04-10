from flask import Flask
from flask_restful import Api

from app.resources import Item


app = Flask(__name__)
api = Api(app)


api.add_resource(Item, '/api/v1/items/<string:key>/')
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
