from setuptools import setup
from codecs import open
from os import path

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboNikto',
    version='1.0',
    packages=[''],
    package_dir={'': 'robonikto'},
    url='https://github.com/we45/RoboNikto',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for Nikto Tool' ,
    install_requires=['robotframework==3.0.4'],
    long_description = long_description,
    long_description_content_type='text/markdown'
)