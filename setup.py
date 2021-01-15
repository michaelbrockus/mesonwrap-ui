#!/usr/bin/env python3

#
# file: setup.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='mesonwrap-ui',
        version='0.1.0',
        author='Michael Brockus',
        license='Apache 2',
        url='https://github.com/michaelbrockus/mesonwrap-ui',
        packages=[
            'code'
        ],
        python_requires='>=3.8',
        entry_points={
            'console_scripts': [
                'mesonwrap-ui=code.main:main_prog',
            ],
        }
    )
