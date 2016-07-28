import os
from setuptools import setup

setup(
    name='archook',
    py_modules=['archook'],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)