from logging import getLogger
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import json

from app.business_logic.services import (
    create_item,
    update_item,
    get_item
)
from app.business_logic.dto import ItemDTO
from app.utils.validators import key_validator, value_validator
from app.utils.exceptions import KeyValidationError, ValueValidationError


logger = getLogger(__name__)


class Item(Resource):
    def get(self, key):
        try:
            key_validator(key=key)
            data = get_item(key=key)
            if data:
                return jsonify(data)
            else:
                return make_response(jsonify(f'Key "{key}" not found.'), 404)

        except KeyValidationError as err:
            logger.debug(err)
            return make_response(
                jsonify('The data did not pass validation.'),
                400
            )

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'key',
            type=str,
            required=True,
            help='This field must be unique and no more than 10 characters.'
        )
        parser.add_argument(
            'value',
            type=str,
            required=True,
            help='This field must be unique and no more than 20 characters.'
        )

        data = parser.parse_args()

        key = data.get('key')
        value = data.get('value')

        try:
            key_validator(key=key)
            value_validator(value=value)

            result = create_item(data=ItemDTO)
            if result:
                return make_response(jsonify(result), 201)
            else:
                return make_response(jsonify(f"Key '{key}' not found."), 404)

        except (KeyValidationError, ValueValidationError) as err:
            logger.debug(err)
            return make_response(
                jsonify('The data did not pass validation.'),
                400
            )
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'key',
            type=str,
            required=True,
            help='This field must be unique and no more than 10 characters.'
        )
        parser.add_argument(
            'value',
            type=str,
            required=True,
            help='This field must be unique and no more than 20 characters.'
        )

        data = parser.parse_args()

        key = data.get('key')
        value = data.get('value')

        try:
            key_validator(key=key)
            value_validator(value=value)

            result = update_item(data=ItemDTO)
            if result:
                return make_response(jsonify(None), 404)
            else:
                return make_response(jsonify(f"Key '{key}' not found."), 404)

        except (KeyValidationError, ValueValidationError) as err:
            logger.debug(err)
            return make_response(
                jsonify('The data did not pass validation.'),
                400
            )
