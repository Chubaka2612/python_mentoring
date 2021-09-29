from distutils.core import setup

# python setup.py sdist
# pip install module_3-1.0.tar.gz
setup(
    name='module_3',
    version='1.0',
    author='Viktoriia Skirko',
    description='Demo project of mentoring task#3',
    packages=['sources'],
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['module_3=sources.demo:main']},
)
