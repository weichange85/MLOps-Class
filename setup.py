from setuptools import setup, find_packages

setup(
    name='jformat',
    version='0.1',
    description='A simple JSON formatter script',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jformat=example_single_file.jformat:main',
        ],
    },
)