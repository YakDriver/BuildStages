# -*- coding: utf-8 -*-
from __future__ import print_function
from math import sin, cos, radians
from rando import __version__
import timeit, sys

def main():
    print("Rando Calculations Test App", __version__)

    result = timeit.repeat('rando.bench()', setup='import rando', number=10, repeat=5)
    result = list(sorted(result))
    print(*result[:3])

if __name__ == "__main__":

    main()
    sys.exit(0)


