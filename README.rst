.. image:: docs/images/logo_readme.jpg
======================================

.. image:: https://travis-ci.org/rafaelcapucho/scrapy-eagle.svg?branch=master
    :target: https://travis-ci.org/rafaelcapucho/scrapy-eagle
    
.. image:: https://img.shields.io/pypi/v/scrapy-eagle.svg
    :target: https://pypi.python.org/pypi/scrapy-eagle
    :alt: PyPI Version
    
.. image:: https://img.shields.io/pypi/pyversions/scrapy-eagle.svg
    :target: https://pypi.python.org/pypi/scrapy-eagle
    
.. image:: https://landscape.io/github/rafaelcapucho/scrapy-eagle/master/landscape.svg?style=flat
    :target: https://landscape.io/github/rafaelcapucho/scrapy-eagle/master
    :alt: Code Quality Status
    
.. image:: https://requires.io/github/rafaelcapucho/scrapy-eagle/requirements.svg?branch=master
    :target: https://requires.io/github/rafaelcapucho/scrapy-eagle/requirements/?branch=master
    :alt: Requirements Status

Scrapy Eagle is a tool that allow us to run any Scrapy_ based project in a distributed fashion and monitor how it is going on and how many resources it is consuming on each server.

.. _Scrapy: http://scrapy.org

**This project is Under Development, don't use it yet**

.. image:: https://badge.waffle.io/rafaelcapucho/scrapy-eagle.svg?label=ready&title=Ready
    :target: https://waffle.io/rafaelcapucho/scrapy-eagle
    :alt: 'Stories in Ready' 

Requeriments
------------

Scrapy Eagle uses Redis_ as Distributed Queue, so you will need a redis instance running.

.. _Redis: http://mail.python.org/pipermail/doc-sig/

Installation
------------

It could be easily made by running the code bellow,

.. code-block:: console

    $ virtualenv eagle_venv; cd eagle_venv; source bin/activate
    $ pip install scrapy-eagle
    
You should create one ``configparser`` configuration file (e.g. in /etc/scrapy-eagle.ini) containing:

.. code-block:: console

    [redis]
    host = 127.0.0.1
    port = 6379
    db = 0
    ;password = someverysecretpass

    [server]
    debug = True
    cookie_secret_key = ha74h3hdh42a
    host = 0.0.0.0
    port = 5000

    [scrapy]
    binary = /project_venv/bin/scrapy
    base_dir = /project_venv/project_scrapy/project

    [commands]
    binary = /project_venv/bin/python3 
    base_dir = /project_venv/project_scrapy/project/commands
    
Then you will be able to execute the `eagle_server` command like,

.. code-block:: console

    eagle_server --config-file=/etc/scrapy-eagle.ini
    
Changes into your Scrapy project
--------------------------------

Enable the components in your `settings.py` of your Scrapy project:

.. code-block:: python

  # Enables scheduling storing requests queue in redis.
  SCHEDULER = "scrapy_eagle.worker.scheduler.DistributedScheduler"

  # Ensure all spiders share same duplicates filter through redis.
  DUPEFILTER_CLASS = "scrapy_eagle.worker.dupefilter.RFPDupeFilter"

  # Schedule requests using a priority queue. (default)
  SCHEDULER_QUEUE_CLASS = "scrapy_eagle.worker.queue.SpiderPriorityQueue"

  # Schedule requests using a queue (FIFO).
  SCHEDULER_QUEUE_CLASS = "scrapy_eagle.worker.queue.SpiderQueue"

  # Schedule requests using a stack (LIFO).
  SCHEDULER_QUEUE_CLASS = "scrapy_eagle.worker.queue.SpiderStack"

  # Max idle time to prevent the spider from being closed when distributed crawling.
  # This only works if queue class is SpiderQueue or SpiderStack,
  # and may also block the same time when your spider start at the first time (because the queue is empty).
  SCHEDULER_IDLE_BEFORE_CLOSE = 0

  # Specify the host and port to use when connecting to Redis (optional).
  REDIS_HOST = 'localhost'
  REDIS_PORT = 6379

  # Specify the full Redis URL for connecting (optional).
  # If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
  REDIS_URL = "redis://user:pass@hostname:6379"
  
Once the configuration is finished, you should adapt each spider to use our Mixin:

.. code-block:: python

    from scrapy.spiders import CrawlSpider, Rule
    from scrapy_eagle.worker.spiders import DistributedMixin
    
    class YourSpider(DistributedMixin, CrawlSpider):
    
        name = "domain.com"
    
        # start_urls = ['http://www.domain.com/']
        redis_key = 'domain.com:start_urls'
        
        rules = (
            Rule(...),
            Rule(...),
        )
        
        def _set_crawler(self, crawler):
            CrawlSpider._set_crawler(self, crawler)
            DistributedMixin.setup_redis(self)

Feeding a Spider from Redis
---------------------------

The class `scrapy_eagle.worker.spiders.DistributedMixin` enables a spider to read the
urls from redis. The urls in the redis queue will be processed one
after another.

Then, push urls to redis::

    redis-cli lpush domain.com:start_urls http://domain.com/

Dashboard Development
---------------------

If you would like to change the client-side then you'll need to have NPM_ installed because we use ReactJS_ to build our interface. Installing all dependencies locally:

.. _ReactJS: https://facebook.github.io/react/
.. _NPM: https://www.npmjs.com/

.. code-block:: console

    cd scrapy-eagle/dashboard
    npm install 

Then you can run ``npm start`` to compile and start monitoring any changes and recompiling automatically.

To generate the production version, run ``npm run build``.

To be easier to test the Dashboard you could use one simple http server instead of run the ``eagle_server``, like:

.. code-block:: console

    sudo npm install -g http-server
    cd scrapy-eagle/dashboard
    http-server templates/

It would be available for you at http://127.0.0.1:8080

**Note**: Until now the Scrapy Eagle is mostly based on https://github.com/rolando/scrapy-redis.
