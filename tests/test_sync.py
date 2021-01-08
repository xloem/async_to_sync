#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for `async_to_sync` package."""

import os
import pytest

def test_example():
    readme = os.path.join(os.path.dirname(__file__), '..', 'README.rst')
    with open(readme) as readme:
        readme = readme.read().split('\n')
    example = [line[4:] for line in readme if line[:4] == '    ' and (len(line) == 4 or line[4] != '$')]
    example = '\n'.join(example)
    exec(compile(example, 'example.py', 'exec'))
