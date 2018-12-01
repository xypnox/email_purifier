# -*- coding: utf-8 -*- 
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epurifier",
    version="0.1.0",
    author="xypnox",
    author_email="xypnox@gmail.com",
    description="A email verifier for csv files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xypnox/email_purifier",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['epurifier=epurifier.main'],
    },
    install_requires = ['pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)