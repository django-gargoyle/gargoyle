#!/usr/bin/env python
import os
import sys

import pytest

# Disable typeguard pytest plugin before importing pytest
os.environ.setdefault("SETUPTOOLS_USE_DISTUTILS", "stdlib")

# Explicitly disable setuptools plugins for pytest
os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.test')
    sys.path.insert(0, 'tests')
    return pytest.main(["-p", "no:typeguard"] + sys.argv[1:])


if __name__ == '__main__':
    sys.exit(main())
