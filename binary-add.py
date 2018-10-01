'''
This is using built in function but not working
'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = bin(a)
        #a1 = "{0:b}".format(a)
        b1 = bin(b)
        #print(a1)
        z = int(a1,2)
        y = int(b1,2)
        
        total = z+y
        return bin(total)[3:]
        
x = Solution()
print(x.addBinary(11,1))