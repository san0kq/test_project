from __future__ import annotations

from redis import Redis
from typing import Optional, TYPE_CHECKING
from flask import current_app

if TYPE_CHECKING:
    from app.data_access.interfaces import DBGatewayProtocol


class RedisGateway:
    """Gateway for interfacing with Redis data store.

    Attributes:
        connection (Redis): Redis connection object.
        _redis_host (str): Redis server hostname.
        _redis_port (int): Redis server port.
        _redis_password (str): Redis server password.

    Methods:
        _create_connection: Create a connection to the Redis server.
        close_connection: Close the connection to the Redis server.
        exists: Check if a key exists in the Redis database.
        get: Retrieve the value associated with a key from the Redis database.
        get_all: Retrieve all keys and their associated values from the Redis database.
        create: Create a new key-value pair in the Redis database.
        update: Update the value of an existing key in the Redis database.
        delete: Delete a key and its associated value from the Redis database.
    """

    def __init__(self) -> None:
        """Initialize the RedisGateway."""
        self._redis_host = current_app.config['REDIS_HOST']
        self._redis_port = current_app.config['REDIS_PORT']
        self._redis_password = current_app.config['REDIS_PASSWORD']
        self.connection = self._create_connection()

    def _create_connection(self) -> Redis:
        """Create a connection to the Redis server."""
        return Redis(
            host=self._redis_host,
            port=self._redis_port,
            password=self._redis_password
        )

    def close_connection(self) -> None:
        """Close the connection to the Redis server."""
        self.connection.close()

    def exists(self, key: str) -> bool:
        """Check if a key exists in the Redis database."""
        return self.connection.exists(key)
    
    def get(self, key: str) -> Optional[dict[str, str]]:
        """Retrieve the value associated with a key from the Redis database."""
        result = self.connection.get(name=key)
        if result:
            return dict(
                key=key,
                value=result.decode('utf-8')
            )
        else:
            return result
    
    def get_all(self) -> list[Optional[dict[str, str]]]:
        """Retrieve all keys and their associated values from the
        Redis database.
        """
        all_keys = self.connection.keys('*')
        result = []
        if all_keys:
            for key in all_keys:
                key = key.decode('utf-8')
                result.append(dict(
                    key=key,
                    value=self.get(key)['value']
                ))

        return result

    def create(self, key: str, value: str) -> None:
        """Create a new key-value pair in the Redis database."""
        self.connection.set(
            name=key,
            value=value
        )
    
    def update(self, key: str, value: str) -> None:
        """Update the value of an existing key in the Redis database."""
        self.create(key=key, value=value)

    def delete(self, key: str) -> None:
        """Delete a key and its associated value from the Redis database."""
        self.connection.delete(key)


class Connection:
    """Connection object for establishing connection to the data source.

    Attributes:
        gateway (DBGatewayProtocol): Data gateway protocol object.

    Methods:
        __enter__: Enter the context for the connection.
        __exit__: Exit the context for the connection.
    """

    def __init__(self, gateway: DBGatewayProtocol) -> None:
        """Initialize the Connection with the provided gateway.

        Args:
            gateway (DBGatewayProtocol): Data gateway protocol object.
        """
        self.gateway = gateway

    def __enter__(self) -> DBGatewayProtocol:
        """Enter the context for the connection."""
        return self.gateway

    def __exit__(self, *args, **kwargs) -> None:
        """Exit the context for the connection."""
        self.gateway.close_connection()
