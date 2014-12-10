"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Test module: utilities to generate test trees

Copyright 2013-2014 Chaim-Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import absolute_import
from intervaltree import Interval, IntervalTree
from pprint import pprint
import test.intervals as intervals
try:
    xrange
except NameError:
    xrange = range


def sdata(s):
    """
    Makes a set of all data fields in an interable of Intervals.
    """
    return set(iv.data for iv in s)


def tree1():
    """Sample IntervalTree for tests."""
    ivs = intervals.ivs1()
    t = IntervalTree(ivs)
    return t


def nogaps_rand(size=100, labels=False):
    """
    Create a random IntervalTree with no gaps or overlaps between
    the intervals.
    """
    return IntervalTree(intervals.nogaps_rand(size, labels))


def gaps_rand(size=100, labels=False):
    """
    Create a random IntervalTree with random gaps, but no overlaps
    between the intervals.
    """
    return IntervalTree(intervals.gaps_rand(size, labels))


if __name__ == "__main__":
    pprint(gaps_rand(labels=False))
