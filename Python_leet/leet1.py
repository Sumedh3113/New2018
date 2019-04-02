class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {} 
        
        for i in range(len(nums)):
        
            if nums[i] in result:
                
                return [result[nums[i]], i]  
                
            else:
                result[target - nums[i]] = i
        



		
'''
First solution without reference solution:-->

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {} #*len(nums)
        remainder = 0
        index = 0
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums:
                index = nums.index(remainder)
                result[remainder] = index 
            else:
                continue
        #print(result)
        
        finalIndex = []
        for i in result:
            finalIndex.insert(result[i],result[i])
        #print(finalIndex)
        return finalIndex
        
        
		


'''