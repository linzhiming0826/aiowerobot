#!/usr/bin/env python

import re
from os import path
from setuptools import setup, find_packages


requirements = [
    'sanic>=22.9.1',
    'xmltodict>=0.12.0',
    'aiohttp>=3.6.2'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = path.join(
    path.dirname(__file__),
    'aiowerobot',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]


setup(
    name='aiowerobot',
    version=version,
    license='MIT',
    url='https://github.com/linzhiming0826/aiowerobot',
    author='TuoX',
    author_email='120549827@qq.com',
    description='一个基础sanic的异步微信公众号开发框架',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements
)
