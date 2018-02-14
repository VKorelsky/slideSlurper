from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='slideSlurper',
    version='1.0.5',
    description='slurp slides from lecture videos',
    url='https://github.com/vkorelsky/slideSlurper',
    author='Victor Korelsky',
    author_email='victor.korelsky@mail.mcgill.ca',
    license='MIT',
    keywords='video capture lectures',
    packages=find_packages('.'),
    install_requires=[
        'tqdm',
        'numpy',
        'Pillow'
        ],
    entry_points={
        'console_scripts': [
            'slurp=slideslurper:main',
        ],
    },
)
