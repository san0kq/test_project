from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from app.resources import Item


app = Flask(__name__)
app.config.from_object('app.config.Config')

SWAGGER_URL = '/api/v1/docs'
API_URL = '/static/swagger/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "REST API APPLICATION"
    },
)

app.register_blueprint(swaggerui_blueprint)

api = Api(app)

api.add_resource(Item, '/api/v1/item/<string:key>/', '/api/v1/item/')
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
