import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as README:
    README = README.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Framework :: Django',
    'Framework :: Django :: 1.10.5',
]

INSTALL_REQUIREMENTS = [
    'Django>=1.10.5',
    'django-webpack-loader>=0.4.1',
    'easy_thumbnails>=2.3',
    'django-filer>=1.2.6',
    'django-mptt>=0.8.7',
    'django-crispy-forms>=1.6.1',
    'django-storages>=1.5.2',
    'djangorestframework>=3.6.3'
]

setup(
    name='django-simplestore',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Simple and tested app that can be taken as a starting point for extending and building custom '
                'ecommerce site with Python / Django.',
    long_description=README,
    url='https://github.com/martinstastny/django-simple-ecommerce',
    author='Martin Stastny',
    author_email='me@martinstastny.cz',
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS
)
