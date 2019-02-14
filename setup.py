import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mdot-rest',
    version='0.1',
    packages=['mdot_rest'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django<1.11,>1.9',
        'djangorestframework<3.9.0',
        'django-filter<2.0',
        'Pillow',
        'mock==1.0.1',
    ],
    license='Apache License, Version 2.0',
    description='A RESTful API server for references to mobile resources.',
    long_description=README,
    url='',
    author='Craig M. Stimmel',
    author_email='cstimmel@uw.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
