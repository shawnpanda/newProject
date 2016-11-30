"""
Online Coding Challenge
Name: Xiang (Shawn) Pan
"""

from collections import defaultdict
import sys

class Anagrams:
    """
	Anagrams: a defaultdict wrapper that maps a key to its anagrams
	"""
    def __init__(self):
        """
		constructor - initialize an empty defaultdict
		"""
        self.container = defaultdict(list)

    def __str__(self):
        """
		String output - string output format for class object
		"""
        res = ""
        for key in self.container:
             res += key + ": " + str(self.container[key]) + " | "
        return res

    def add(self, word):
        """
        add - Converts the given word into a lower cased and sorted key,
        and then appends the word to the list corresponding to the key.
        Args:
            word: A string value read from the dictionary
        """
        # Converts word to a lower cased and sorted key
        key = ''.join(sorted(word.lower()))
        self.container[key].append(word)

    def check(self, word):
        """
        check - Converts the given word into a lower cased and sorted key,
        and then returns the list corresponding to the key.
        Args:
            word: A string value read from the user input
        """
        # Converts word to a lower cased and sorted key
        key = ''.join(sorted(word.lower()))
        return self.container[key]

    def sortLists(self):
        """
        sortLists - A helper function that is called after all the dictionary
        words are read to sort all the string values in lexicographical order
        in each list.
        """
        for key in self.container:
            self.container[key].sort(key=lambda w: w.lower())
            self.container[key] = " ".join(self.container[key])
"""
Main Program
Args:
    argv: Expects a string argument as the path to the dictionary file
"""
def main(argv):
    # Offline step starts
    anagrams = Anagrams()
    # Opens the file according to the command line argument
    f = open(argv[1], 'r')
    # Reads in each word in each line
    for word in f:
        anagrams.add(word.rstrip())
    f.close()
    anagrams.sortLists()
    # Offline step ends

    # Online step starts
    while True:
        userInput = raw_input(">")
        if not userInput: break
        res = anagrams.check(userInput)
        print "-" if res == [] else res
    # Online step ends and program quits

if __name__ == "__main__":
    main(sys.argv)
