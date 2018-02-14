from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slideSlurper',
    version='1.0.0',
    description='slurp slides from lecture videos',
    long_description=long_description,
    url='https://github.com/vkorelsky/slideSlurper',
    author='Victor Korelsky',
    author_email='victor.korelsky@mail.mcgill.ca',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Other audience',
        'Topic :: Multimedia :: Video :: Conversion',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'

        # untested with versions superior to python 2.7
    ],

    keywords='video capture lectures',

    packages=find_packages('.'),

    install_requires=[
        'tqdm',
        'cv2',
        'numpy',
        'fdpf',
        'PIL'
        ],

    entry_points={
        'console_scripts': [
            'slurp=slideSlurper:main',
        ],
    },
)
