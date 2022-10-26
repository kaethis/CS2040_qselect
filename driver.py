#!/usr/bin/env python3


# -----------------------------------------------------------------------------
""" ...
""" # -------------------------------------------------------------------------

__author__ = '@kaethis'

__version__ = '1.1'


import argparse

import curses

import qselect

import util


def prog(stdscr): # -----------------------------------------------------------
    """ This FUNCTION ...
    """ # ---------------------------------------------------------------------

    global qs


    # NOTE: This program presumes the terminal is capable of displaying color.

    # TODO: Check to see whether or not the terminal is capable of displaying
    #       colors.  If it cannot, skip over color pair initialization and
    #       opt for basic color palette instead.

    colors = {\
        12 : (500,   0, 500),\
        13 : (  0,   0, 500),\
        14 : (500,   0,   0),\
        15 : (250, 250, 250),\
        16 : (  0, 500,   0),\
        17 : (750, 500,   0),\
        18 : (500, 500, 500),\
    }

    for c in colors.keys():

        curses.init_color(c, colors[c][0], colors[c][1], colors[c][2])


    color_pairs = {\
        1 : (curses.COLOR_WHITE, curses.COLOR_BLACK),\
        2 : (curses.COLOR_WHITE, 12),\
        3 : (curses.COLOR_WHITE, 13),\
        4 : (curses.COLOR_WHITE, 14),\
        5 : (curses.COLOR_BLACK, 15),\
        6 : (curses.COLOR_BLACK, curses.COLOR_WHITE),\
        7 : (curses.COLOR_WHITE, 16),\
        8 : (17,                 curses.COLOR_BLACK),\
        9 : (18,                 curses.COLOR_BLACK),\
    }

    for p in color_pairs.keys():

        curses.init_pair(p, color_pairs[p][0], color_pairs[p][1])


    # Calculate loop invariants and predicates for later conditionals:

    elems_len = len(qs.elems)

    elem_width = max(len(str(e)) for e in qs.elems)     # Number of digits of
                                                        # largest integer in
                                                        # list.


    # Calculate stdscr dimensions (i.e. terminal screen):

    screen_ymax, screen_xmax = stdscr.getmaxyx()
   

    # Calculate win dimensions:

    win_yoffs, win_xoffs = 1, 2     # Number of spaces win offset from origin
                                    # (0,0) of stdscr.

    win_padding = 2                 # Number of spaces between edge of win
                                    # (including box border) and cells.

    win_ymax = (screen_ymax-win_xoffs-(win_padding*2))
                                                     
    win_xmax = (screen_xmax-win_yoffs-(win_padding*2))

   
    # Calculate cell dimensions:

    cell_margin = 1                             # Number of spaces b/w cells.

    cell_width = (elem_width+cell_margin)

    cell_height = (2+cell_margin)

    cell_ymax = int(win_ymax/cell_height)       # Total num of cells per col.

    cell_xmax = int(win_xmax/cell_width)        # Total num of cells per row.

   
    index_max = ((cell_ymax*cell_xmax)-1)

    index_width = len(str(index_max))           # Number of digits of maximum
                                                # allowable index.

    # If number of digits of maximum allowable index greater than the number of
    # digits of largest integer in list, base cell width off number of digits
    # of index instead:

    if (index_width > elem_width):

        cell_width = (index_width+cell_margin)

        cell_xmax = int(win_xmax/cell_width)    # Recalculate total number of
                                                # cells per row.
    

    # Validate screen size sufficient for displaying entire list of integers
    # according to dimensions calculated above:

    if (elems_len > (index_max+1)):

        raise BufferError("screen size insufficient")


    win = stdscr.subwin(\
        ((cell_height*cell_ymax)+(win_padding*2)-cell_margin),\
        ((cell_width*cell_xmax)+(win_padding*2)-cell_margin),\
        win_yoffs,\
        win_xoffs\
    )

    win.box()


    is_pivot = False    # Whether or not last pivot is k-th smallest element.


    while True:

        for i in range(0, cell_ymax):

            for j in range(0, cell_xmax):

                cell_i = ((i*cell_xmax)+j)

                
                if (0 <= cell_i < elems_len):

                    elem = qs.elems[cell_i]


                    if (cell_i == qs.lo) and (cell_i == qs.hi):

                        p = curses.color_pair(2)    # If index both segment
                                                    # start and segment end,
                                                    # color index WHITE/PURPLE.

                    elif (cell_i == qs.lo):

                        p = curses.color_pair(3)    # If index segment start,
                                                    # color index WHITE/RED.

                    elif (cell_i == qs.hi):

                        p = curses.color_pair(4)    # If index segment end,
                                                    # color index WHITE/BLUE.

                    elif (cell_i < qs.lo) or (cell_i > qs.hi):

                        p = curses.color_pair(5)    # If index outside segment,
                                                    # color index BLACK/GREY.

                    else:

                        p = curses.color_pair(6)    # If index inside segment,
                                                    # color index BLACK/WHITE.


                    win.move(\
                        ((i*cell_height)+win_padding),\
                        ((j*cell_width)+win_padding)\
                    )

                    win.addstr(str(cell_i).rjust(cell_width-cell_margin), p)


                    if (cell_i == qs.s):

                        if (cell_i == (qs.k-1)):
                            
                            p = curses.color_pair(7)    # If elem both pivot
                                                        # and k-th smallest
                                                        # element, color elem
                                                        # WHITE/GREEN.

                        else: 

                            p = curses.color_pair(8)    # If elem pivot but
                                                        # not k-th smallest
                                                        # element, color elem
                                                        # ORANGE/BLACK.

                    elif (cell_i < qs.lo) or (cell_i > qs.hi):

                        p = curses.color_pair(9)    # If elem outside segment,
                                                    # color elem GREY/BLACK.

                    else:

                        p = curses.color_pair(1)    # If elem inside segment,
                                                    # color elem WHITE/BLACK.
                                                    
                    win.move(\
                        ((i*cell_height)+win_padding+1),\
                        ((j*cell_width)+win_padding)\
                    )

                    win.addstr(str(elem).rjust(cell_width-cell_margin), p)


        win.refresh()


        stdscr.move(0, 0)       # Move cursor somewhere inconsequential.

        match stdscr.getch():   # Block for keypad input and capture key code.

            # In case key code match with keypad constant for screen resize,
            # recalculate only those dimensions affected and resize win
            # according to new dimensions:

            case curses.KEY_RESIZE:

                screen_ymax, screen_xmax = stdscr.getmaxyx()

            
                win_ymax = (screen_ymax-win_xoffs-(win_padding*2))

                win_xmax = (screen_xmax-win_yoffs-(win_padding*2))


                cell_width = (elem_width+cell_margin)

                cell_ymax = int(win_ymax/cell_height)

                cell_xmax = int(win_xmax/cell_width)


                index_max = ((cell_ymax*cell_xmax)-1)

                index_width = len(str(index_max))

                if (index_width > elem_width):

                    cell_width = (index_width+cell_margin)

                    cell_xmax = int(win_xmax/cell_width)


                # Validate screen size sufficient for displaying entire list of
                # integers according to new dimensions calculated above:

                if (elems_len > (index_max+1)):

                    raise BufferError("screen size insufficient")


                stdscr.clear()  # Clear stdscr (i.e. terminal screen).


                win.resize(\
                    ((cell_height*cell_ymax)+(win_padding*2)-cell_margin),\
                    ((cell_width*cell_xmax)+(win_padding*2)-cell_margin)\
                )

                win.box()

                win.refresh()


            # In case key code match any other keypad constant ...

            case _:

                # If last pivot not k-th smallest element, ensue next iteration
                # of quicksort and capture whether or not latest pivot is k-th
                # smallest element; otherwise, break out of loop:

                if not is_pivot:

                    is_pivot = qs.step()

                else:

                    break


def exit(): # -----------------------------------------------------------------
    """ This FUNCTION exits the program.
    """ # ---------------------------------------------------------------------

    global qs

   
    # Print the list of elements after final iteration of the algorithm, the
    # value of the pivot (which is now the k-th smallest element) and which of
    # two partitioning schemes used:

    print(qs.elems)

    print("{0}-th smallest element is {1} (using ".format(qs.k, qs.getPivot())\
        + ("Hoare's " if qs.is_hoare else "Lomuto's ")\
        + "partitioning algorithm).")


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


    curses.wrapper(prog)


    exit()  # Exit the program formally.


if __name__ == '__main__': main()
