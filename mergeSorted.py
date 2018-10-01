class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        num3 =[]
        for _ in range(m+n):
            num3.append(0)
        #print(num3)
        
        for i in range(n,m+n,1):
            nums1[i] = nums2[n-1]
        
        for i in range(m+n):
            for j in range(n):
                    #print(j)
                    if nums1[i] > nums2[j]:
                        num3[i] = nums2[j]
                        print(i)
                        break
                    else:
                        num3[i] = nums1[i]
        
        print(num3)
        
x = Solution()
x.merge([1,2,3,0,0,0],3,[2,5,6],3)