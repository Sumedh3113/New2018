class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == "":
            return 0
            
        elif target in nums:
            return nums.index(target)
        
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    continue
                else :
                    return i
            return len(nums)
