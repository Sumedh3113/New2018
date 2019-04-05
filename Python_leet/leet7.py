class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        num = abs(x)
        
        if(x < 0):
            sign = -1
        while num:
            rem = num % 10
            num = num//10
            rev = rev*10 + rem 
        #print(rev)
        if(rev > 2**31 - 1 or rev < -2**31):
            return 0

        
        return sign*rev