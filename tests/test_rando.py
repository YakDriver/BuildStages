# -*- coding: utf-8 -*-
"""Rando main test module."""

import pytest
from rando import cli

def test_bench():
    cli.main()
    
    assert True
