from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from app.data_access.dao import ItemDAO
from app.data_access.db_connector import RedisGateway, Connection
from app.data_access.exceptions import (
    KeyDoesNotExistError,
    KeyAlreadyExistsError
)
from app.logger.logger import get_logger

if TYPE_CHECKING:
    from app.business_logic.dto import ItemDTO


logger = get_logger(__name__)


def get_item(data: ItemDTO) -> Optional[dict[str, str]]:
    """This function retrieves an item from the database based on the provided 
    ItemDTO data.

    Parameters:
    data (ItemDTO): The data transfer object containing information about the 
    item to retrieve.

    Returns:
    Optional[dict[str, str]]: Returns the value of the retrieved item as a string if it
    exists. Returns None if the item does not exist.

    Raises:
        None
    """
    dao = ItemDAO(connection=Connection(gateway=RedisGateway()))
    try:
        result = dao.get(data=data)
        logger.info(
            f'The key "{data.key}" and its value have been retrieved in'
            f'response to the query.'
        )
        return result
    except KeyDoesNotExistError as err:
        logger.info(err)
        return None


def get_all() -> list[Optional[dict[str, str]]]:
    """Retrieve all keys and their corresponding values from the data source.

    Returns:
        list[Optional[dict[str, str]]]: A list containing all keys and their
        associated values.

    Raises:
        None
    """
    dao = ItemDAO(connection=Connection(gateway=RedisGateway()))
    result = dao.get()
    logger.info(
        f'The keys and values from the database were retrieved'
        f'in the amount of: {len(result)}.')
    return result


def create_item(data: ItemDTO) -> Optional[ItemDTO]:
    """Create a new item in the data source.

    Args:
        data (ItemDTO): The data transfer object containing information about
        the item to be created.

    Returns:
        Optional[ItemDTO]: The created item data transfer object if successful,
        otherwise None.

    Raises:
        None
    """
    dao = ItemDAO(connection=Connection(gateway=RedisGateway()))
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


def update_item(data: ItemDTO) -> bool:
    """Update the value of an existing item in the data source.

    Args:
        data (ItemDTO): The data transfer object containing information about
        the item to be updated.

    Returns:
        bool: True if the item was successfully updated, False otherwise.

    Raises:
        None
    """
    dao = ItemDAO(connection=Connection(gateway=RedisGateway()))

    try:
        dao.update(data=data)
        logger.info(
            f'The value of the key "{data.key}" has been updated '
            f'to "{data.value}".'
        )
        return True
    except KeyDoesNotExistError as err:
        logger.info(err)
        return False


def delete_item(data: ItemDTO) -> bool:
    """Delete an item from the data source.

    Args:
        data (ItemDTO): The data transfer object containing information about
        the item to be deleted.

    Returns:
        bool: True if the item was successfully deleted, False otherwise.

    Raises:
        None
    """
    dao = ItemDAO(connection=Connection(gateway=RedisGateway()))

    try:
        dao.delete(data=data)
        logger.info(f'The key {data.key} has been successfully deleted.')
        return True
    except KeyDoesNotExistError as err:
        logger.info(err)
        return False
