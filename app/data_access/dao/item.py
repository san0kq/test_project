from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseDAO
from app.data_access.exceptions import (
    KeyAlreadyExistsError,
    KeyDoesNotExistError
)

if TYPE_CHECKING:
    from app.business_logic.dto import ItemDTO
    from redis import Redis


class ItemDAO(BaseDAO):
    def create(self, data: ItemDTO) -> None:
        conn = self._db_gateway
        if self._db_gateway.exists(data.key):
            self._db_gateway.close_connection()
            raise KeyAlreadyExistsError(
                f'The key "{data.key}" already exists in the database.'
            )
        conn.create(
            key=data.key,
            value=data.value
        )
        self._db_gateway.close_connection()

    def get(self, data: ItemDTO) -> str:
        conn = self._db_gateway
        result = conn.get(data.key)
        self._db_gateway.close_connection()

        if not result:
            raise KeyDoesNotExistError(
                f'The key "{data.key}" does not exist in the database'
            )

        return result

    def update(self, data: ItemDTO) -> list[str]:
        conn = self._db_gateway
        if not conn.exists(data.key):
            self._db_gateway.close_connection()
            raise KeyDoesNotExistError(
                f'The key "{data.key}" does not exist in the database'
            )
        else:
            conn.update(
                name=data.key,
                value=data.value
            )
            self._db_gateway.close_connection()
