import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='django-reportmail',
    version='1.0',
    packages=['reportmail'],
    url='https://github.com/hirokiky/django-reportmail',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='django library to render and send report mail. ',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    install_requires=[
        'Django>=1.6,<1.7',
    ],
    include_package_data=True,
    zip_safe=False,
)
