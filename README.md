## CS 2040 - Algorithms I
**Assignment #4:** Quickselect; Lomuto and Hoare's Partitioning Algorithms

**Author:** Matt W. Martin

### About

This program features a nonrecursive implementation of *quickselect*, a selection algorithm for finding the *k*-th smallest element in an unordered list, using either [Lomuto's partitioning algorithm](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme) or [Hoare's algorithm](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme) as its partitioning scheme.

---
### Contents
The contents of this repository include the following files:
```
./
    README.md        # this file
    driver.py        # for executing the program
    integers.txt     # a list of integers (from textbook on p.160)
    qselect.py       # implementation and data structures for quickselect
    util.py          # helper functions
```

---
### Dependencies
This program requires the following modules from the Python 3.10 standard library:
```
argparse    # parser for command-line options, args and sub-commands
math        # mathematical functions (namely, ceil)
os          # misc operating system interfaces (namely, file i/o)
re          # regular expression operations
typing      # support for type hints
```

---
### Instructions
Program execution instructions can be found by entering `python3 driver.py --help`:
```
...
```
...

---
### Links
Here are some resources I found useful when developing this program:

- [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html) This program features a variety of different types of arguments made possibly by the argparse library, each with their own associated behaviour.  The documentation explains how to achieve these results.

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) Here's a definitive list of every single built-in exception Python has to offer; especially useful for when trying to determine which exception to raise is most appropriate.
