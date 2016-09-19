# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2013)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

"""This module attaches the HDF5 input output methods to the FrequencySeries.
"""

from ...types.io import hdf5
from .. import (FrequencySeries, SpectralVariance)

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'

for array_type in (FrequencySeries, SpectralVariance):
    hdf5.register_hdf5_array_io(array_type)
    hdf5.register_hdf5_array_io(array_type, format='hdf', identify=False)