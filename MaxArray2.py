# Time Complexity is O(n^2)
def maxDiff(array):
    maxdiffer = float('-inf')
    
    for i in range(len(array)-1,-1,-1):
        j = 0
        while j < i:
            diff = array[i] - array[j]
            #print(str(array[i]) +'- '+ str(array[j]) +'='+ str(diff))
            if (maxdiffer < diff):
                maxdiffer = diff
            j +=1
    if(maxdiffer < 0):
        return -1
    return maxdiffer    

array = [7,2,3,10,2,4,8,1]
array2 = [4,1,0]

show = maxDiff(array)
print(show)
show = maxDiff(array2)
print(show)