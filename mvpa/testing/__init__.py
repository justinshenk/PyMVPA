# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the PyMVPA package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Helpers to unify/facilitate unittesting within PyMVPA

"""

__docformat__ = 'restructuredtext'

from mvpa.base import externals
from mvpa import pymvpa_dataroot

if __debug__:
    from mvpa.base import debug
    debug('INIT', 'mvpa.testing')

from mvpa.testing.tools import *

if __debug__:
    from mvpa.base import debug

    _all_ca_enabled = 'ENFORCE_STATES_ENABLED' in debug.active
else:
    _all_ca_enabled = False

from sweepargs import sweepargs

if __debug__:
    debug('INIT', 'mvpa.testing end')
