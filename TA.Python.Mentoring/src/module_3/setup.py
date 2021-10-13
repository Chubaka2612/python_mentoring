from setuptools import setup

# python setup.py sdist
# pip install module_3-1.0.tar.gz
from setuptools import find_packages

setup(
    name='module_3',
    version='1.0',
    author='Viktoriia Skirko',
    description='Demo project of mentoring task#3',
    packages=find_packages(include=['sources']),
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['module_3=sources.demo:main']},
)
