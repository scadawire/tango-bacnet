README 
======

This repository contains the code for a PyTANGO Device Server for communicating with devices via BACnet IP protocol. 
This code was acquired by SKAO in 2021 and relicensed under a 3-clause BSD license.

Some changes to port to newer dependency / newer tango version as of 2022:
* package ported to python3
* PyTango changed to tango python package
* bacpypes newer version compatibility

There are some outstanding issues with the code base should be resolved in order to enhance this package:
* the package is missing tests
* BACnetDS uses the tango low-level API. It should be rewritten to use the high-level API.

Requirement 
-----------

- setuptools
- PyTango >= 8.1.6
- BACpypes == 0.14.1

Run in terminal, to install requirements:

        pip install -r requirements.txt


Installation
------------

1) Download bacnet
2) Extract it into the folder (e.g. c://BacNet)
3) Launch the command prompt.
4) Move into folder bacnet (cd c://BacNet)
5) Run python setup.py install
6) Run program with BacNetDS