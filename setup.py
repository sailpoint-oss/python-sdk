# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "sailpoint"
VERSION = "1.1.8"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0", "python-dateutil", "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="The SailPoint API SDK for Python",
    author="SailPoint Developer Relations",
    author_email="developer-relations@sailpoint.com",
    url="https://developer.sailpoint.com/",
    keywords=["OpenAPI", "OpenAPI-Generator", "SailPoint", "SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_data={"sailpoint": ["py.typed"]},
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Documentation": "https://developer.sailpoint.com/idn/tools/sdk/python",
        "Issues": "https://github.com/sailpoint-oss/python-sdk/issues"
    }
)
