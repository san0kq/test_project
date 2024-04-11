from __future__ import annotations

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from flask import Response

from app.business_logic.services import (
    create_item,
    update_item,
    get_item,
    get_all,
    delete_item
)
from app.business_logic.dto import ItemDTO
from app.utils.validators import key_validator, value_validator
from app.utils.exceptions import KeyValidationError, ValueValidationError
from app.logger.logger import get_logger

logger = get_logger(__name__)


class Item(Resource):
    """Resource for handling item-related HTTP requests.

    Methods:
        get: Handle GET requests for retrieving items.
        post: Handle POST requests for creating items.
        put: Handle PUT requests for updating items.
        delete: Handle DELETE requests for deleting items.
    """

    def get(self, key: Optional[str] = None) -> Response:
        """Handle GET requests for retrieving items.

        Args:
            key (str, optional): The key of the item to retrieve.
            Defaults to None.

        Returns:
            Response: JSON response containing the retrieved item or items.
        """
        if key:
            try:
                key_validator(key=key)
                data = get_item(data=ItemDTO(key=key))
                if data:
                    return jsonify(data)
                else:
                    return make_response('', 404)

            except KeyValidationError as err:
                logger.debug(err)
                return make_response('', 400)
        else:
            data = get_all()
            return jsonify(data)

    def post(self, key: Optional[str] = None) -> Response:
        """Handle POST requests for creating items.

        Args:
            key (str, optional): The key of the item to create.
            Defaults to None.

        Returns:
            Response: JSON response containing the created item or an
            error message.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'key',
            type=str,
            required=True,
            help='This field must be unique string and no more than 10 characters.'
        )
        parser.add_argument(
            'value',
            type=str,
            required=True,
            help='This field must be string and no more than 20 characters.'
        )

        data = parser.parse_args()

        key = data.get('key')
        value = data.get('value')

        try:
            key_validator(key=key)
            value_validator(value=value)

            result = create_item(data=ItemDTO(key=key, value=value))
            if result:
                return make_response(jsonify(result), 201)
            else:
                return make_response('', 403)

        except (KeyValidationError, ValueValidationError) as err:
            logger.debug(err)
            return make_response('', 400)
    
    def put(self, key: Optional[str] = None) -> Response:
        """Handle PUT requests for updating items.

        Args:
            key (str, optional): The key of the item to update.
            Defaults to None.

        Returns:
            Response: JSON response containing the updated item or an
            error message.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'key',
            type=str,
            required=True,
            help='This field must be unique string and no more than 10 characters.'
        )
        parser.add_argument(
            'value',
            type=str,
            required=True,
            help='This field must be tring and no more than 20 characters.'
        )

        data = parser.parse_args()

        key = data.get('key')
        value = data.get('value')

        try:
            key_validator(key=key)
            value_validator(value=value)

            result = update_item(data=ItemDTO(key=key, value=value))
            if result:
                return make_response('', 204)
            else:
                return make_response('', 404)

        except (KeyValidationError, ValueValidationError) as err:
            logger.debug(err)
            return make_response('', 400)

    def delete(self, key: str) -> Response:
        """Handle DELETE requests for deleting items.

        Args:
            key (str): The key of the item to delete.

        Returns:
            Response: JSON response indicating success or failure of
            the deletion.
        """
        try:
            key_validator(key=key)
            result = delete_item(data=ItemDTO(key=key))
            if result:
                return make_response('', 204)
            else:
                return make_response('', 404)

        except KeyValidationError as err:
            logger.debug(err)
            return make_response('', 400)
