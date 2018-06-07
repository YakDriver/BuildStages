# -*- coding: utf-8 -*-
"""
Provides the entry point for a standard benchmark test.
"""

import timeit, sys

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)
from rando import __version__


def main():
    print("Rando Calculations Test App", __version__)

    result = timeit.repeat('rando.bench()', setup='import rando', number=10, repeat=5)
    result = list(sorted(result))
    print(*result[:3])

if __name__ == "__main__":

    main()
    sys.exit(0)


