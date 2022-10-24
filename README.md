## CS 2040 - Algorithms I
**Assignment #4:** Quickselect; Lomuto and Hoare's Partitioning Algorithm

**Author:** Matt W. Martin

### About

This program ...


---
### Contents
The contents of this repository include the following files:
```
./
    README.md        # this file
    driver.py        # for executing the program
    qselect.py       # implementation and data structure for ...
    util.py          # helper function(s)
    integers.txt     # a list of integers (from textbook on p.160)
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
