.. image:: docs/images/logo_readme.jpg
======================================

Scrapy Eagle is a tool that allow us to run any Scrapy based project in a distributed fashion and monitor how it is going on and how many resources it is consuming on each server.

**This project is Under Development, don't use it yet**

Installation
------------

It could be easy made by running the code bellow,

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

Note: Scrapy Eagle use parts of https://github.com/rolando/scrapy-redis
