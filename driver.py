#!/usr/bin/env python3


# -----------------------------------------------------------------------------
""" ...
""" # -------------------------------------------------------------------------

__author__ = '@kaethis'

__version__ = '1.0'


import argparse

import qselect

import util


def prog(): # -----------------------------------------------------------------
    """ This FUNCTION ...
    """ # ---------------------------------------------------------------------

    global qs


    while True:

        if qs.step():

            break


def exit(): # -----------------------------------------------------------------
    """ This FUNCTION exits the program.
    """ # ---------------------------------------------------------------------

    global qs

    
    for i in range(0, len(qs.elems)):

        print("{:03d}".format(i), end=' ')

    print()


    for elem in qs.elems:

        print("{:3d}".format(elem), end=' ')

    print()


    elem = qs.getPivot()

    print("{0}-th smallest element is {1}, using ".format(qs.k, elem)\
        + ("Hoare's " if qs.is_hoare else "Lomuto's ")\
        + "partitioning algorithm.")


    quit()


def main(): # -----------------------------------------------------------------
    """ This MAIN FUNCTION ...
    """ # ---------------------------------------------------------------------

    global qs


    parser = argparse.ArgumentParser(\
        description= "This PROGRAM features a nonrecursive implementation of\
                      quickselect using either Lomuto's partitioning algorithm\
                      or Hoare's algorithm as its partitioning scheme.",\
        epilog=      "~created by " + __author__\
    )

    parser.add_argument(\
        'ints',\
        metavar= 'N',\
        type=    int,\
        nargs=   '*',\
        help=    "a list of one or more integers (separated by spaces)"\
    )

    parser.add_argument(\
        '--file',\
        metavar= 'PATH',\
        type=    util.validateFile,\
        help=    "path to a file containing one or more integers (separated by\
                  some delimiter)"\
    )

    parser.add_argument(\
        '--k',\
        type=    int,\
        help=    "number for the k-th smallest element in a list of integers\
                  (default is median)"\
    )

    parser.add_argument(\
        '--hoare',\
        action= argparse.BooleanOptionalAction,\
        help=   "whether or not to use Hoare's partitioning algorithm (default\
                 is Lomuto's algorithm)"\
    )


    args = parser.parse_args()


    # Initialize the list of integer numbers from arguments.  If a list of one
    # or more ints (metavar N) and file (metavar PATH) both provided, the
    # integers from the file are appended to the end of the list:

    nums = args.ints if args.ints is not None else []

    nums += args.file if args.file is not None else []


    # Validate list of integer numbers (nums) not empty:

    if (len(nums) == 0):

        raise argparse.ArgumentTypeError(\
            "one or more integers must be provided"\
        )

    # If number for the k-th smallest element (k) provided from arguments,
    # validate k within bounds:

    if args.k is not None and not (0 < args.k <= len(nums)):

        raise argparse.ArgumentTypeError(
            "bad k-th position: '{0}' (min:1, max:{1})"\
                .format(args.k, len(nums))\
        )


    qs = qselect.QuickSelector(nums, args.hoare, args.k)


    prog()


    exit()  # Exit the program formally.


if __name__ == '__main__': main()
