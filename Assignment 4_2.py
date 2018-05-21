"""
Created on Mon May 21 15:52:50 2018   @author: krishna.i
Assignment 4.2
######################################################
Problem​ ​Statement​ ​1: Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint:​ ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
######################################################
"""
def myFunc(myStr):      # This function builts a list of list of integers corresponding to length of words in a list
    myLs = myStr.split()    # Splitting a given string into a list of words
    print("The list of Words supplied: ", myLs)
    myNumLs = []
    for a in myLs:
        myNumLs.append(a.__len__())     # Appending the list with length value of each word in the list
    return myNumLs      # Returning the final list variable containing numeric values

sampleStr = input("Please enter a string of words: ")   # Accepting a string or words
print("Output list of integers representing lengths of corresponding words is: ", myFunc(sampleStr)) # Function call

"""
######################################################
Problem​ ​Statement​ ​2: Write a Python function which takes a character (i.e. a string of length 1) and 
returns True if it is a vowel, False otherwise.
######################################################
"""
def chkVowel(myChar):       # This function checks if a single char is entered and returns True if its a Vowel
    if myChar.__len__() > 1 :
        print("Oops...Please ensure that you are typing a single character..!")
        return
    Vowel = ['a','e','i','o','u']   # Creating a list of character string values containing Vowel characters
    if myChar.lower() in Vowel:
        return True
    else:
        return False

myChr = input("Please enter a Char: ")
if chkVowel(myChr):     # Calling the Check Vowel function and printing the return value
    print("The given Char is a Vowel as function has returned: ", True)
else:
    print("The given Char is not a Vowel as function has returned: ",False) 