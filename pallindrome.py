"""Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""

''' My Solution do not check for words with spaces provided ans is better'''
def palindrome(s):
    rev = s[::-1]
    if(s==rev):
        return True
    else:
        return False
    
#---Actual Solution didn't thought about spaces Good # 

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1] # Check through slicing