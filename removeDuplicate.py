class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        y = list(s)
        
         if nums == []:
            return 0
       
        #print(y)
        j =0
        for i in range(len(y)):
            #print(i)
            nums[i] = y[i]
            #print(i)
            
        del nums[len(y)]    #j +=1
        #print(nums)
        
        return len(nums)
x = Solution()
print(x.removeDuplicates([1,1,2]))
