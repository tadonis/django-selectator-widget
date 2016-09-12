# -*- coding: UTF-8 -*-

"""
 Copyright (c) 2016, TP-Link Co.,Ltd.
 Author:  tanghuifeng <tanghuifeng@tp-link.net>
 Created: 2016/9/12
"""

import os
from setuptools import setup, find_packages

__version__ = '1.0.0'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-selectator-widget",
    version=__version__,
    description="Django select widget which is friendly and functionality",
    long_description=read('README.md'),
    keywords="django select selectator",
    url='https://github.com/asyncee/django-easy-select2',
    download_url='',
    author='tadonis',
    author_email='tanghf1988@126.com',
    license='MIT',
    packages=find_packages(exclude=['test_project']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Django Widget Sets',
    ],
    zip_safe=False,
)
