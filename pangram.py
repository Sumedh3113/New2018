"""
Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" 
"""
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1.lower()
    if alphabet in str1:
        return True
    else:
        return False
    
#---Actual Solution----#
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    #print(set(str1.lower())) 
    return alphaset <= set(str1.lower())  #here we are creating two sets one contains all the alphabet and other contains letter 
#from the string then alphabet set should be <= set of string as it might contains two letters repeatedly 


