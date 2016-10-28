# -*- coding: utf-8 -*-

import os
import io
from setuptools import setup, find_packages


LONG_DESC = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


def read_file(filename):
    with io.open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
        if not line.startswith('#')]


setup(name='scrapy-eagle',
    version='0.0.37',
    description='Run Scrapy Distributed',
    long_description=LONG_DESC,
    author='Rafael Alfredo Capucho',
    author_email='rafael.capucho@gmail.com',
    url='http://github.com/rafaelcapucho/scrapy-eagle',
    packages=find_packages(),
    license='BSD',
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,
    entry_points={
        'console_scripts': ['eagle_server=scrapy_eagle.dashboard.main:entry_point'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
    ],
)
