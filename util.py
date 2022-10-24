#!/usr/bin/env python3


# -----------------------------------------------------------------------------
""" This MODULE contains helper functions and data structures outside the scope
    of the problem domain.
""" # -------------------------------------------------------------------------

__author__ = '@kaethis'

__version__ = '1.0'


import os

import re

from argparse import ArgumentTypeError

from typing import Tuple


def validateFile(path: str) -> Tuple[int, ...]: # -----------------------------
    """ This FUNCTION validates a file, specified by its path, contains one or
        more integers (separated by some delimiter) and returns any integers
        contained in the file as a tuple.
    """ # ---------------------------------------------------------------------

    if os.path.isdir(path):

        raise ArgumentTypeError("is a directory: '{}'".format(path))


    try:

        fd = os.open(path, os.O_RDONLY)

        data = os.read(fd, os.path.getsize(path)).decode("utf-8")

    
        ints = tuple(int(i) for i in re.findall(r"(\d+)", data))

        assert (len(ints) != 0)


        os.close(fd)

    except FileNotFoundError:

        raise ArgumentTypeError("not found: '{}'".format(path))

    except IOError:

        raise ArgumentTypeError("cannot read: '{}'".format(path))

    except AssertionError:

        raise ArgumentTypeError("contains no integers: '{}'".format(path))


    return ints
