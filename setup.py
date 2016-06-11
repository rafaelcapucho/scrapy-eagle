import os
from setuptools import setup


LONG_DESC = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(name='scrapy-eagle',
    version='0.0.2',
    description='Run Scrapy Distributed',
    long_description=LONG_DESC,
    author='Rafael Alfredo Capucho',
    author_email='rafael.capucho@gmail.com',
    url='http://github.com/rafaelcapucho/scrapy-eagle',
    packages=['scrapy_eagle.worker', 'scrapy_eagle.dashboard'],
    license='BSD',
    install_requires=['Scrapy>=1.1.0', 'redis>=2.10.0'],
    entry_points = {
        'console_scripts': ['eagle_server=scrapy_eagle.dashboard.server:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
    ],
)
