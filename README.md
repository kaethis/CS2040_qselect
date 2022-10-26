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
    README.md       # this file
    driver.py       # for executing the program
    example1.txt    # a list of integers (from textbook on p.160)
    example2.txt    # a list of more integers (from random number generator)
    qselect.py      # implementation and data structures for quickselect
    util.py         # helper functions
```

---
### Dependencies
This program requires the following modules from the Python 3.10 standard library:
```
argparse    # parser for command-line options, args and sub-commands
curses      # terminal handling for character-cell displays
math        # mathematical functions (namely, ceil)
os          # misc operating system interfaces (namely, file i/o)
re          # regular expression operations
typing      # support for type hints
```

---
### Instructions
Program execution instructions can be found by entering `python3 driver.py --help`:
```
usage: driver.py [-h] [--file PATH] [--k K] [--hoare | --no-hoare] [N ...]

This PROGRAM features a nonrecursive implementation of quickselect using either
Lomuto's partitioning algorithm or Hoare's algorithm as its partitioning scheme.

positional arguments:
  N                    a list of one or more integers (separated by spaces)

options:
  -h, --help           show this help message and exit
  --file PATH          path to a file containing one or more integers
                       (separated by some delimiter)
  --k K                number for the k-th smallest element in a list of
                       integers (default is median)
  --hoare, --no-hoare  whether or not to use Hoare's partitioning algorithm
                       (default is Lomuto's algorithm)

~created by @kaethis
```
A list of integer numbers can be provided as a positional command-line argument (separated by spaces) and/or a path to a file containing one or more integers (separated by some delimiter) using the `--file PATH` option.  If a list of one or more integers and file path are both provided, the integers from the file are appended to the end of the list.  The median of the list is selected if no number for the *k*-th smallest element is provided with `--k K`.  Hoare's partitioning algorithm is used by specifying the `--hoare` option; Lomuto's algorithm is used by default (or by explicitly specifying `--no-hoare`).

For example, the program will select the *2nd* smallest integer in an unordered list of integers *128, 2, 32, 4, 256, 1, 64, 8 and 16* using Hoare's partitoning algorithm by entering `python3 driver.py 128 2 32 4 256 1 64 8 16 --k 2 --hoare` (whereby the integer selected will by *2*).

Alternatively, the program will select the *median* of an unordered list of integers specified in a file called *example1.txt* containing the integers *4, 1, 10, 8, 7, 12, 9, 2 and 15* using Lomuto's algorithm by entering `python3 driver.py --file example1.txt` (whereby the integer selected will be *8*).

This program will segment the list of integers according to its start and end indices (called *lo* and *hi*, respectively) about a pivot (the first element in the segment) until the pivot is the *k*-th smallest integer.  The *lo* index is colored in blue whereas the *hi* index is colored red; if *lo* equals *hi*, the index is colored purple.  The value of the last pivot is colored orange until the pivot equals the *k*-th smallest integer, after which it will be colored green.  Proceed to the next iteration of the algorithm by pressing any key on the keyboard.

After the *k*-th smallest integer is selected, the list of integers after the final iteration of quicksort will be printed to the console alongside the integer selected and partitioning scheme used:

```
[2, 1, 4, 7, 8, 12, 9, 10, 15]
5-th smallest element is 8 (using Lomuto's partitioning algorithm).
```

---
### Links
Here are some resources I found useful when developing this program:

- [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html) This program features a variety of different types of arguments made possibly by the argparse library, each with their own associated behaviour.  The documentation explains how to achieve these results.

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) Here's a definitive list of every single built-in exception Python has to offer; especially useful for when trying to determine which exception to raise is most appropriate.

- [RANDOM.ORG - Integer Generator](https://www.random.org/integers/) Random number generator where the the randomness comes from atmospheric noise.  Pretty cool!
