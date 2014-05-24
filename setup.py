import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='django-reportmail',
    version='1.0b1',
    packages=find_packages('reportmail'),
    url='https://github.com/hirokiky/django-reportmail',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='django library to render and send report mail. ',
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
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
