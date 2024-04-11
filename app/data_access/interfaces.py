from typing import Protocol, Any


class DBGatewayProtocol(Protocol):
    """Protocol for defining the interface of a data gateway.

    Attributes:
        connection: Connection attribute.
        close_connection: Method for closing the connection.
        create: Method for creating a new item in the data source.
        update: Method for updating an existing item in the data source.
        delete: Method for deleting an item from the data source.
        get: Method for retrieving an item from the data source.
        get_all: Method for retrieving all items from the data source.
        exists: Method for checking if an item exists in the data source.
    """
    connection: Any
    close_connection: Any
    create: Any
    update: Any
    delete: Any
    get: Any
    get_all: Any
    exists: Any
