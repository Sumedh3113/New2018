class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stri = ''
        for i in digits:
            stri += str(i) 
        
        ints = int(stri)
        #print(ints)
        result = ints + 1
        f = [int(i) for i in str(result)]
        #f = result.split()
        return f
            
