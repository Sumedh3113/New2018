class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        #sub = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        #print(s.split('',1))
        for char in (s):
            # if s[i] == 'I'  and s[i+1] == 'V' or s[i+1] == 'X':
            #     sub = -1
            # if s[i] == 'X'  and s[i+1] == 'L' or s[i+1] == 'C':
            #     sub = -10
            # if s[i] == 'C'  and s[i+1] == 'D' or s[i+1] == 'M':
            #     sub  = -100
            total += roman[char] 
            
        return total