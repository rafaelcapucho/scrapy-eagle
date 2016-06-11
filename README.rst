.. image:: docs/images/logo_readme.jpg
======================================

Scrapy Eagle is a tool that allow us to run any Scrapy_ based project in a distributed fashion and monitor how it is going on and how many resources it is consuming on each server.

.. _Scrapy: http://scrapy.org

**This project is Under Development, don't use it yet**

Requeriments
------------

Scrapy Eagle uses Redis_ as Distributed Queue, so you will need a redis instance running.

.. _Redis: http://mail.python.org/pipermail/doc-sig/

Installation
------------

It could be easily made by running the code bellow,

.. code-block:: console

    $ pip install scrapy-eagle
    
You should create one ``configparser`` configuration file (e.g. in /etc/scrapy-eagle.ini) containing:

.. code-block:: console

    [redis]
    host = 10.10.10.10
    port = 6379
    db = 0
    
Then you will be able to execute the `eagle_server` command like,

.. code-block:: console

    eagle_server --config=/etc/scrapy-eagle.ini
    
Usage
-----

Enable the components in your `settings.py` of your Scrapy project:

.. code-block:: python

  # Enables scheduling storing requests queue in redis.
  SCHEDULER = "scrapy_eagle.worker.scheduler.DistributedScheduler"

  # Schedule requests using a priority queue. (default)
  SCHEDULER_QUEUE_CLASS = 'sscrapy_eagle.worker.queue.SpiderPriorityQueue'

  # Schedule requests using a queue (FIFO).
  SCHEDULER_QUEUE_CLASS = 'scrapy_eagle.worker.queue.SpiderQueue'

  # Schedule requests using a stack (LIFO).
  SCHEDULER_QUEUE_CLASS = 'scrapy_eagle.worker.queue.SpiderStack'

  # Max idle time to prevent the spider from being closed when distributed crawling.
  # This only works if queue class is SpiderQueue or SpiderStack,
  # and may also block the same time when your spider start at the first time (because the queue is empty).
  SCHEDULER_IDLE_BEFORE_CLOSE = 0

  # Specify the host and port to use when connecting to Redis (optional).
  REDIS_HOST = 'localhost'
  REDIS_PORT = 6379

  # Specify the full Redis URL for connecting (optional).
  # If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
  REDIS_URL = 'redis://user:pass@hostname:9001'

**Note**: Until now the Scrapy Eagle is mostly based on https://github.com/rolando/scrapy-redis.
