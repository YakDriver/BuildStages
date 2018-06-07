# -*- coding: utf-8 -*-
from __future__ import print_function
from math import sin, cos, radians
import timeit

__version__ = "0.0.1"

""" 
This is a pointless Python program to do something for a while to
roughly test AppVeyor and Travis and various configurations
unrelated to this computing.

All credit: https://gist.github.com/apalala/3fbbeb5305584d2abe05
"""

def bench():
    product = 1.0
    for counter in range(1, 1000, 1):
        for dex in list(range(1, 360, 1)):
            angle = radians(dex)
            product *= sin(angle)**2 + cos(angle)**2
            product -= counter**4
            product += 1
            product += counter**4
            product -= 1
    return product
    