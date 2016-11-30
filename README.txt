Online Coding Challenge
Name: Xiang (Shawn) Pan

###Implementation Details
- Implementation language - Python 2.7.11
- Python collections library

I am using defaultdict class from the python collections library and initialize the values to be lists. When words are read from the dictionary, I create a key by setting the word to be lower case and sorting each character by alphabetical order. I then use that key to access the corresponding list and append the original dictionary word to the list.
After the dictionary file is read, I then loop through all the list items in the container object and format all the values to the desired output string style. When the user inputs a string to check anagrams, I convert the word to the corresponding key by lower casing and sorting to find the output value.

###To run:
python anagrams.py path-to-dict.txt

1. What is the running time of your program (separately the offline and the online steps), in
terms of asymptotic complexity? Be careful about naming your variables
 (i.e., O(N) doesn’t mean much unless you specify what N is).

Running time of offline step: O(M(log(N) + log(M))) where M is the number of all the words in the dictionary and N is the average string length of words in the dictionary.
Running time of online step: O(Nlog(N)) where N is the length of the user string input.

2. How much memory does your program consume, also in terms of asymptotic complexity?

Memory consumed: O(M) where M is the number of all the words in the dictionary.


3. [Extra Credit - Don’t spend time on this until you’ve finished the main
 assignment] Suppose you did not have enough memory to preprocess all of the results - for example, the dictionary has a million words, but you only have 2MB
 memory. What additional steps would you have to take to solve this problem?

I would find ways to preprocess the words so that I can identify words uniquely and size of the preprocessed results will be smaller than that of the original string.
In addition, I would consider modify the dictionary file if its editable and map my structure to the file.
