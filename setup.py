# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="py-zapcli",
    version="0.1.0",
    description="Quick CLI helpers to start control OWASP ZAP by headless",
    license="MIT",
    author="Niko Phung<niko0xdev@gmail.com>",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
    ],
    packages=[
        "cli",
        "cli.commands",
    ],
    install_requires=[
        "click==4.0",
        "python-owasp-zap-v2.4==0.0.14",
        "requests==2.20.1",
        "tabulate==0.7.5",
        "termcolor==1.1.0",
        "six==1.10.0",
    ],
    extras_require={
        "dev": [
            "coverage==3.7.1",
            "ddt==1.0.1",
            "mock==2.0.0",
            "pep8==1.6.2",
            "pylint==1.5.5",
            "pytest==3.0.7",
            "responses==0.5.1",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "zap-cli=cli.cli:cli",
        ],
    },
    test_suite="tests",
)
