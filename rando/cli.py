# -*- coding: utf-8 -*-
"""Provides the entry point for a standard benchmark test."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

import sys
import timeit

from rando import __version__


def main():
    """Run test when using CLI."""
    print("Rando Calculations Test App", __version__)

    result = timeit.repeat(
        'rando.bench()',
        setup='import rando',
        number=10,
        repeat=5
    )
    result = list(sorted(result))
    print(*result[:3])


if __name__ == "__main__":

    main()
    sys.exit(0)
