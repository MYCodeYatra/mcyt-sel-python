from setuptools import setup
setup(
    name='pytest-mycodeyatra-selenium',
    version='0.1.0',
    description='A custom PyTest plugin for enterprise Selenium configuration',
    author='MyCodeYatra',
    py_modules=['pytest_mycodeyatra'],
    install_requires=['pytest', 'selenium'],
    # THIS IS THE MAGIC LINE!
    entry_points={
        'pytest11': [
            'mycodeyatra = pytest_mycodeyatra',
        ],
    },
)