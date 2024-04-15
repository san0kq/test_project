import unittest
import redis

from app.app import app
from app.config import REDIS_TEST_PORT, APP_HOST


class BaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.redis = redis.Redis(host=APP_HOST, port=REDIS_TEST_PORT)
        app.config['REDIS_HOST'] = APP_HOST
        app.config['REDIS_PORT'] = REDIS_TEST_PORT
        app.config['REDIS_PASSWORD'] = None
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self) -> None:
        self.redis.flushall()
        self.ctx.pop()


if __name__ == "__main__":
    unittest.main()
