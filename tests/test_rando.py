# -*- coding: utf-8 -*-
"""Rando main test module."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)
from rando import cli


def test_bench():
    """
    Tests the whole kit.
    """
    cli.main()

    assert True
