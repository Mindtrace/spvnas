""" Setup
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spvnas',
    description='SPVNAS for PyTorch',

    keywords='pytorch pretrained efficientdet efficientnet bifpn object detection',
    packages=find_packages(),
    install_requires=['torch >= 1.4'],
    python_requires='>=3.6',
)
