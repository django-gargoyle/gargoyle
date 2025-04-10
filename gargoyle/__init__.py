"""
gargoyle
~~~~~~~~

:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""
from __future__ import absolute_import, division, print_function

from django.utils.module_loading import autodiscover_modules

from gargoyle.manager import gargoyle

__version__ = '2.1.2'
VERSION = __version__  # old version compat

__all__ = ('gargoyle', 'autodiscover', '__version__', 'VERSION')


def autodiscover():
    """
    Auto-discover INSTALLED_APPS' gargoyle modules and fail silently when
    not present. This forces an import on them to register any gargoyle bits they
    may want.
    """
    import gargoyle.builtins  # noqa
    autodiscover_modules('gargoyle')
