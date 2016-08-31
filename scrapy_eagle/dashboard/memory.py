import json

import redis

from scrapy_eagle.dashboard.settings import get_config_file

redis_pool = None


def init_memory():

    global redis_pool

    config = get_config_file()

    redis_pool = redis.ConnectionPool(
        host=config['redis']['host'],
        port=config['redis']['port'],
        db=config['redis']['db'],
        password=config.get('redis', 'password', fallback='')
    )


def get_redis_pool():
    return redis_pool


def get_connection():

    if not redis_pool:
        init_memory()

    return redis.Redis(connection_pool=redis_pool)


def get_job_object(key):

    redis_conn = get_connection()

    json_obj = redis_conn.get('eagle_jobs:{key}'.format(key=key))

    if json_obj:
        return json.loads(json_obj.decode('utf-8'))
    else:
        return None


if __name__ == "__main__":

    from scrapy_eagle.dashboard.settings import setup_configuration

    _config = setup_configuration(config_file='/etc/scrapy-eagle.ini')

    init_memory()

    o = get_job_object(key='epocacosmeticos.com.br')
    print(o.get('priority'))
