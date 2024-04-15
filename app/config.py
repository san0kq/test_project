import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')


REDIS_TEST_PORT = os.environ.get('REDIS_TEST_PORT', 6377)
APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
