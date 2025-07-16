from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = [r for r in f.read().splitlines() if "-e " not in r]

setup(
    name='localstorage',
    version='0.2',
    packages=find_packages(),
    install_requires=requirements, 
    include_package_data=True,
)
