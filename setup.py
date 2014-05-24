from setuptools import setup, find_packages

setup(
    name='django-reportmail',
    version='0.1',
    packages=find_packages('reportmail'),
    url='https://github.com/hirokiky/django-reportmail',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='django library to render and send report mail. ',
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
