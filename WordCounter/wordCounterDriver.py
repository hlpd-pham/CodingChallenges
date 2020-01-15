"""
- This program reads in a paragraph from an input file and generates a histogram
of the words used sorted from most occurrences to least. The output will consist 
of the word followed by a pipe character ("|"), a number of equal signs that are 
proportional to the number of occurrences found in the text, and the number of 
occurrences itself. The generated histogram will be stored in an output file (output.txt)
- Sample Input:
    Hickory, dickory, dock.
    The mouse ran up the clock. The clock struck one,
    The mouse ran down, Hickory, dickory, dock.
- Sample Output:
        the | ==== (4)
    hickory | == (2)
    dickory | == (2)
       dock | == (2)
      mouse | == (2)
        ran | == (2)
      clock | == (2)
         up | = (1)
     struck | = (1)
        one | = (1)
       down | = (1)

Command Parameters
------------------
    python3 wordCounterDriver.py inputFile

Results
-------
    - All output is written to output file (output.txt).

Notes
-----
    - The program ignores case sensitivity from the input file
    - All special characters from the input file will be filtered out.
    - This program will call functions from WordCounter.py
"""

import sys
import os
from WordCounter import WordCounter

# validate number of input arguments
if len(sys.argv) < 2:
    print("filename needed as command argument")
    sys.exit(1)

filename = sys.argv[1]

# validate input file
if os.path.isfile(filename) == False:
    print(f"Error: {filename} is not a file.")
    print("Exit Program")
    sys.exit(1)

wc = WordCounter(filename)
wc.generateHistogram()
