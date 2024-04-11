from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.data_access.db_connector import Connection


class BaseDAO:
    """Base Data Access Object (DAO) for interacting with a data source.

    Attributes:
        connection (Connection): The connection object used to establish
        connection to the data source.

    Methods:
        __init__: Initializes the BaseDAO object with the provided connection.
    """
    def __init__(self, connection: Connection) -> None:
        """Initialize the BaseDAO with the provided connection.

        Args:
            connection (Connection): The connection object used to establish
            connection to the data source.
        """
        self.connection = connection
