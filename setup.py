# /usr/bin python

import os

from setuptools import setup

VERSION = "0.0.1"
PROJECT_NAME = "SoftwareHelper"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(BASE_DIR, 'README.rst')

with open(README, 'r') as f:
    long_description = f.read()


setup(
    name='ProjectHelper',
    version=VERSION,
    description='Project generator for software creating by the Python programming language',
    long_description=long_description,
    url='https://github.com/setivolkylany/ProjectHelper',
    author='setivolkylany',
    author_email='setivolkylany@gmail.com',
    license='BSD',
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='python utils programming',
    packages=[],
    install_requires=[
        'ipdb>=0.10.0',
        'ipython>=5.1.0',
        'factory_boy>=2.7.0',
        'invoke>=0.13.0',
        'Pillow>=3.4.2',
        'python-dateutil>=2.6.0',
        'Unipath>=1.1',
    ],
    extras_require={
        'dev': [

        ],
        'test': [

        ],
    },
    entry_points={
        'console_scripts': [
            'project-helper = {}.main:main'.format(PACKAGE_NAME),
        ],
    },
)
