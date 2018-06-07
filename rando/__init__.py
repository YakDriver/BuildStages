# -*- coding: utf-8 -*-
"""
Rando is a semi-pointless Python program.

Rando Calculations does something for a while to
roughly test AppVeyor and Travis and various configurations
unrelated to this computing.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

from math import cos, radians, sin

__version__ = "0.0.1"


def bench():
    """
    Rerforms a benchmark with computations.

    Based largely on
    https://gist.github.com/apalala/3fbbeb5305584d2abe05
    """
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
