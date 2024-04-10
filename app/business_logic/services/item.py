from logging import getLogger

from app.business_logic.dto import ItemDTO
from app.data_access.dao import ItemDAO
from app.data_access.db_connector import RedisGateway
from app.data_access.exceptions import (
    KeyDoesNotExistError,
    KeyAlreadyExistsError
)

logger = getLogger(__name__)


def get_item(key):
    dao = ItemDAO(db_gateway=RedisGateway())
    try:
        result = dao.get(data=ItemDTO(key=key))
        logger.info(
            f'The key "{key}" and its value have been retrieved in response '
            f'to the query.'
        )
        return result
    except KeyDoesNotExistError as err:
        logger.info(err)
        return None

def create_item(data: ItemDTO):
    dao = ItemDAO(db_gateway=RedisGateway())

    try:
        dao.create(data=data)
        logger.info(
            f'A new key has been added - "{data.key}", with the '
            f'value "{data.value}".'
        )
        return data
    except KeyAlreadyExistsError as err:
        logger.info(err)
        return None

def update_item(data: ItemDTO):
    dao = ItemDAO(db_gateway=RedisGateway())

    try:
        dao.update(data=data)
        logger.info(
            f'The value of the key "{data.key}" has been updated '
            f'to "{data.value}".'
        )
        return data
    except KeyDoesNotExistError as err:
        logger.info(err)
        return None
