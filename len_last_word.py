"""
Finds the length of last word
.strip() is used to strips the white spaces 
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s and s.strip():
            ss = s.split()
            return len(ss[-1])
        else:
            return 0
