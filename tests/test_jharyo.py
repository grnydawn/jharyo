#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `jharyo` package."""



import os
import pytest

from jharyo import jharyo

here = os.path.dirname(os.path.abspath(__file__))
sample1 = here + '../data/sample1.csv'
sample2 = here + '../data/sample2.csv'

@pytest.fixture
def fix():
    """Sample pytest fixture.
    """

def test_parallel(fix):
    """Sample pytest test function with the pytest fixture as an argument."""

    argv = [
        'sample1.csv', 'sample2.csv',
        '--parallel', '[[d0], [d1]]',
    ]
    assert jharyo.main(argv) == 0
