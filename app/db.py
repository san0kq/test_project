from redis import Redis
from app.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

redis = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
