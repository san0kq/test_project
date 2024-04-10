from redis import Redis
from app.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisGateway:
    def __init__(self) -> None:
        self.connection = self._create_connection()

    def _create_connection(self) -> Redis:
        return Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def close_connection(self):
        self.connection.close()

    def exists(self, key):
        return self.connection.exists(key)
    
    def get(self, key):
        return self.connection.get(name=key)
    
    def create(self, key, value):
        self.connection.set(
            name=key,
            value=value
        )
    
    def update(self, key, value):
        self.create(key=key, value=value)
