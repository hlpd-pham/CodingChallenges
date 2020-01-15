import sys
import os
import re
import collections
from collections import defaultdict

class WordCounter():

    def __init__(self, inputFileName):
        self.wordCountDict, self.longestWordLength = self.generateWordCount(inputFileName)

    def generateHistogram(self):
        """
        Generate a output of the word count of each word in wordCountDict.
        The output consists of the word followed by a pipe character ("|"), 
        a number of equal signs that are proportional to the number of 
        occurrences found in the text, and the number of occurrences itself.

        Outputs
        -------
            output.txt file that contains the word counts from wordCountDict.
        """
        outputFileName = 'output.txt'
        with open(outputFileName, 'w') as outputFile:
            for word in sorted(self.wordCountDict, key=self.wordCountDict.get, reverse=True):
                # indent the word so that the pipe symbol of its count
                # can line up with the longest word
                indentSpaces = ( self.longestWordLength - len(word) ) * ' '
                count = self.wordCountDict[word]
                print(f"{indentSpaces}{word} | {count*'='} ({count})", file = outputFile)

    def generateWordCount(self, inputFileName):
        """
        - Opens the file with given name and populates a dictionary which contains the 
        counts of number of occurences of each word from the input file. 
        - Stores the length of the longest word from the input file.

        Parameters
        ----------
        inputFileName: str
            name of input file

        Returns
        -------
        dict
            A dictionary that stores the count of occurences of each word from
            the input file.
        int
            Length of the longest word from the input file.
        """
        wordCountDict = defaultdict(int)
        longestWordLength = -1

        with open(inputFileName, 'r') as inputFile:
            while True:
                inputLine = inputFile.readline()

                if inputLine == "": # EOF
                    break
                
                # get rid of new line characters of original line
                inputLine = inputLine.rstrip('\n')	
										           
                # get rid of leading and trailing whitespaces of each stripped input line
                line = inputLine.lstrip().rstrip()

                # if the is empty, go to the next one
                if line == '':
                    continue

                # split the line into tokens
                tokens = line.split(' ')

                # process each token 
                for token in tokens:
                    # filter out special characters in the token
                    word = self.filterSpecialCharacters(token)
                    # check if word has longer length than current longestWordLength
                    longestWordLength = max(len(word), longestWordLength)
                    # add the word count 
                    wordCountDict[word] += 1 

        return wordCountDict, longestWordLength

    def filterSpecialCharacters(self, token):
        # filter out special characters and transform it into lowercase word and return the result
        return re.sub('[^A-Za-z0-9]+', '', token).lower()