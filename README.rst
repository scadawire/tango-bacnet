README 
======

This repository contains the code for a PyTANGO Device Server for communicating with devices via BACnet IP protocol. 
This code was acquired by SKAO in 2021 and relicensed under a 3-clause BSD license. 
There are some outstanding issues with the code base that will have to be resolved in order to make use of this package
effectively: 

* the package is missing tests
* bacpypes 0.14.1 was released in Aug 2016, since then the module layout has changed. Changes in BACnetDS would be needed to upgrade to a later version.
* the package needs to be ported to Python3, this is mostly related to print statements. 
* BACnetDS uses the PyTango low-level API. It will need to be rewritten to use the high-level API. 

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
2) Extract itinto thefolder(e.g. c://BacNet)
3) Launch the command prompt.
4) Move into folder bacnet(cd c://BacNet)
5) Run python setup.py install



