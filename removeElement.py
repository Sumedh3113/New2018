class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        #print(nums)
        #nums.append('X')
        x = len(nums)
        countr =0
        
        for i in range(x-1,-1,-1):
            #print(i)
            if nums[i] == val:
                #print(nums[i])
                nums.pop(i)
                #nums.append('X')
                
                #countr +=1
            else:
                continue
                    
            
        #print(countr)
        #print(len(nums))
        result = len(nums)
        return result    

                
s = Solution()
#numb = [1,2,2,2,3]
numb =[1]
print(s.removeElement(numb,1))
print(numb)