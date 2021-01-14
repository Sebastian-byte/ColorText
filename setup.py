from setuptools import setup, find_packages
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = open(path.join("./", "VERSION"))

setup(
    name = "Python-ColorText",
    version = version_file.read().strip(),
    license = "GPL v3",
    author = "Sebastian Montoya",
    author_email = "sebastianmontoya209@gmail.com",
    description = "Color Strings in Python easily",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sebastian-byte/ColorText",
    packages = find_packages(),
    install_requires = [
       "colorama",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.4"
)
