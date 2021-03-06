import json
from setuptools import setup, find_packages

if __name__ == '__main__':
    with open('setup.json', 'r') as handle:
        kwargs = json.load(handle)
    setup(
        include_package_data=True,
        packages=find_packages(),
        setup_requires=[
            'reentry'
        ],
        reentry_register=True,
        **kwargs
    )