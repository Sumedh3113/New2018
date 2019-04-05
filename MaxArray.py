# time complexity O(n)
def maxDiff(a, arr_size): 
    max_diff = float('-inf') 
    min_element = float('inf') 
      
    for i in range(arr_size): 
        min_element = min(min_element, a[i])
        #if(min_element == a[i]):
        #    continue
        max_diff= max(max_diff,a[i] - min_element)
    #if(max_diff == float('-inf')):
    #    return 0
    if(max_diff <= 0):
        s = set(a)
		# checking for equality here
        if(len(a) > len(s)):
            return 0
        return -1
        
    return max_diff 
      
# Driver program to test above function  
arr = [8,4]
size = len(arr) 
print ("Maximum difference is",  
        maxDiff(arr, size)) 
