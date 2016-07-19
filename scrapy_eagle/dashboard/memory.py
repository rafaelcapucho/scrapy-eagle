import redis

from scrapy_eagle.dashboard.config import get_config

redis_pool = None

def init_memory():

    global redis_pool

    config = get_config()

    redis_pool = redis.ConnectionPool(
        host=config['redis']['host'],
        port=config['redis']['port'],
        db=config['redis']['db']
    )

def get_redis_pool():
    return redis_pool

def get_connection():

    if not redis_pool:
        init_memory()

    return redis.Redis(connection_pool=redis_pool)

def testando():
    pass