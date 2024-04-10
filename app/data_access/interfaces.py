from typing import Protocol, Any


class DBGatewayProtocol(Protocol):
    connection: Any
    close_connection: Any
    create: Any
    update: Any
    get: Any
    exists: Any
