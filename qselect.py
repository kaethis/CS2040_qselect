#!/usr/bin/env python3


# -----------------------------------------------------------------------------
""" This MODULE ...
""" # -------------------------------------------------------------------------

__author__ = '@kaethis'

__version__ = '1.0'


from math import ceil

from typing import Any, Optional, List


class QuickSelector(): # ------------------------------------------------------
    """ This CLASS ...
    """ # ---------------------------------------------------------------------

    def __init__(self,\
            elems: List[Any], is_hoare: bool = False, k: Optional[int] = None
        ): # ------------------------------------------------------------------
        """ This CONSTRUCTOR ...
        """ # -----------------------------------------------------------------

        self.elems = elems          # The list of comparable elements.

        self.is_hoare = is_hoare    # Whether or not to use Hoare's partition
                                    # algorithm; if not, Lomuno's algorithm is
                                    # used instead.

        # Number of k-th smallest element in the list of comparable elements.
        # If no such number provided for k, select median instead:
        
        self.k = ceil(len(self.elems)/2) if k is None else k


        self.lo = 0                         # Start index of segment of list.

        self.hi = (len(self.elems)-1)       # End index of segment of list.

        self.s = -1                         # Index of pivot of the segment
                                            # (-1 indicates not yet segmented).
        

    def step(self) -> bool: # -------------------------------------------------
        """ This FUNCTION ...
        """ # -----------------------------------------------------------------

        self.s = self.hoare(self.elems, self.lo, self.hi) if self.is_hoare\
            else self.lomuto(self.elems, self.lo, self.hi)


        if (self.s < (self.k-1)):

            # If index of pivot is less than (k-1), partition segment after the
            # pivot.

            self.lo = (self.s+1)

        elif (self.s > (self.k-1)):

            # If index of pivot is greater than (k-1), partition segment before
            # the pivot.

            self.hi = (self.s-1)

        else:

            # If index of pivot equals (k-1), the pivot is the k-th smallest
            # element.

            return True


        return False


    def getPivot(self) -> Any: # ----------------------------------------------
        """ This FUNCTION returns the pivot element in the list.
        """ # -----------------------------------------------------------------

        if (self.s == -1):

            raise IndexError("list not yet segmented")


        return self.elems[self.s]

        
    def lomuto(self, elems: List[Any], lo: int, hi: int) -> int: # ------------
        """ This FUNCTION partitions a segment of a list (specified by start
            and end indices lo and hi, respectively, and lo <= hi) by Lomuto's
            algorithm using the first element of the segment as its pivot (p)
            and returns the new index of p (s) after partitioning, whereby all
            elements before it are <= p and all elements after it are >= p.
        """ # -----------------------------------------------------------------

        p = elems[lo]   # Use first element of section as pivot.


        s = lo

        for i in range((lo+1), (hi+1)):

            if (elems[i] < p):

                s += 1

                elems[i], elems[s] = elems[s], elems[i]


        elems[lo], elems[s] = elems[s], elems[lo]

        return s


    def hoare(self, elems: List[Any], lo: int, hi: int) -> int: # -------------
        """ This FUNCTION partitions a segment of a list (specified by start
            and end indices lo and hi, respectively, and lo < hi) by Hoare's
            algorithm using the first element of the segment as its pivot (p)
            and returns the new index of p (j) after partitioning, whereby all
            elements before it are <= p and all elements after it are >= p.
        """ # -----------------------------------------------------------------

        p = elems[lo]   # Use first element of section as pivot.

        # NOTE: Since index i can go out of the list's bounds, rather than
        #       checking this condition every time i is incremented, a sentinel
        #       is appended to the list to prevent i from advancing beyond the
        #       size of list.

        elems.append(p)


        i, j = lo, (hi+1)

        while True:

            i += 1

            while (elems[i] < p): i += 1    # Scan from left side of segment
                                            # until elem. is greater than or
                                            # equal to pivot.
            j -= 1

            while (elems[j] > p): j -= 1    # Scan from right side of segment
                                            # until elem. is less than or equal
                                            # to pivot.

            elems[i], elems[j] = elems[j], elems[i]


            if (i >= j):

                elems[i], elems[j] = elems[j], elems[i]     # Undo last swap.

                break


        elems.pop()     # NOTE: Remove sentinel from list.


        elems[lo], elems[j] = elems[j], elems[lo]

        return j
