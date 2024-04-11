from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .base import BaseDAO
from app.data_access.exceptions import (
    KeyAlreadyExistsError,
    KeyDoesNotExistError
)

if TYPE_CHECKING:
    from app.business_logic.dto import ItemDTO


class ItemDAO(BaseDAO):
    """Data Access Object (DAO) for interacting with item data in the data source.

    Inherits From:
        BaseDAO: Base Data Access Object for interacting with a data source.

    Methods:
        create: Create a new item in the data source.
        get: Retrieve an item from the data source.
        update: Update the value of an existing item in the data source.
        delete: Delete an item from the data source.
    """

    def create(self, data: ItemDTO) -> None:
        """Create a new item in the data source.

        Args:
            data (ItemDTO): The data transfer object containing information about the item to be created.

        Raises:
            KeyAlreadyExistsError: If the provided key already exists in the data source.
        """
        with self.connection as connection:
            if connection.exists(data.key):
                raise KeyAlreadyExistsError(
                    f'The key "{data.key}" already exists in the database.'
                )
            connection.create(
                key=data.key,
                value=data.value
            )

    def get(self, data: ItemDTO = None) -> Optional[
        dict[str, str] | list[Optional[dict[str, str]]]
        ]:
        """Retrieve an item from the data source.

        Args:
            data (ItemDTO, optional): The data transfer object containing information about the item to be retrieved.
                                       Defaults to None.

        Returns:
            Optional[dict[str, str] | list[Optional[dict[str, str]]]: The value associated with the provided key,
            or a list containing all keys and their associated values if no key is provided.
            Returns None if the key does not exist.

        Raises:
            KeyDoesNotExistError: If the provided key does not exist in the data source.
        """
        with self.connection as connection:
            if data:
                result = connection.get(data.key)
                if not result:
                    raise KeyDoesNotExistError(
                        f'The key "{data.key}" does not exist in the database'
                    )
            else:
                result = connection.get_all()

            return result

    def update(self, data: ItemDTO) -> None:
        """Update the value of an existing item in the data source.

        Args:
            data (ItemDTO): The data transfer object containing information about the item to be updated.

        Raises:
            KeyDoesNotExistError: If the provided key does not exist in the data source.
        """
        with self.connection as connection:
            if not connection.exists(data.key):
                raise KeyDoesNotExistError(
                    f'The key "{data.key}" does not exist in the database'
                )
            else:
                connection.update(
                    key=data.key,
                    value=data.value
                )
    
    def delete(self, data: ItemDTO) -> None:
        """Delete an item from the data source.

        Args:
            data (ItemDTO): The data transfer object containing information about the item to be deleted.

        Raises:
            KeyDoesNotExistError: If the provided key does not exist in the data source.
        """
        with self.connection as connection:
            if not connection.exists(data.key):
                raise KeyDoesNotExistError(
                    f'The key "{data.key}" does not exist in the database'
                )
            else:
                connection.delete(
                    key=data.key
                )
