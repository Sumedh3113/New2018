# -ve numbers do not satisfy the criteria of palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
                
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
            
        
            return sign*rev
        
        num = x
        reverse =  reverse(self,x)
     
        if(reverse >= 0 and num == reverse):
            return True
        return False
