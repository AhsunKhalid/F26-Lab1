
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
# Use the string method .upper() to convert the name to upper case.
# Create another variable called “age”, the value of “age” should be your age
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 

#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.

words= "the quick brown fox jumps over the lazy dog"
print(words[0]) #first character
print(words[16]) 

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.
slice1= words[ -23:-18]
print(slice1)
#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
slice3=words[2:15]
print(slice3)
# Print "uick brown foxs ju" from "words".
print(words[5:22])