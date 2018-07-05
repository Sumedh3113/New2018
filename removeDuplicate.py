class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        y = list(s)
        
        y = sorted(y)
        if nums == []:
            return 0
       
        #print(y)
        
        for i in range(len(y)):
            #print(i)
            nums[i] = y[i]
            #print(nums[i])
        
        for i in range(len(y),len(nums)):
            #if(i != len(nums)-1):
            del nums[len(y)] 
            #else:
            #    print("I am screwed")
        
        return len(nums)
x = Solution()
print(x.removeDuplicates([-1,0,3]))
