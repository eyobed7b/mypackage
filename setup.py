from setuptools import setup, find_packages


setup(
    name="myPackage",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description="EDSA example python package",
    long_description= open("README.md").read(),
    requires = ["numpy"],
    url="https://github.com/eyobed7b/mypackage",
    author="eyobed.feleke",
    author_email="eyobed7b@gmail.com"
)