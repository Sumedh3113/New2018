"""
Input: ["aad","ccd","c"]

Output: []

"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s =""
        count = 0
        flag =1
        
        
        if(strs == []):
            return s
        
        x = len(strs[0])
        for i in range(len(strs)):
            if(i != len(strs)-1):
                #print(len(strs[i]))
                if(len(strs[i+1]) <= x):
                    x = len(strs[i+1])
                else:
                    continue
        #print(x)
                
            
        if(len(strs) == 1):
            s +=strs[0]
            return s
        
        for i in range(x):
            #print(i)
            for j in range(len(strs)):
                #number += 1
                #print(j ," ", number )
                if(j < len(strs)-1):
                    #print(j)
                    if(strs[0][i] == strs[j+1][i]):
                        if (j+1 == len(strs)-1):
                            count +=1
                        continue
                    #This condition is added to check every character 
					else:
                        flag =0
                        break
            if(flag == 0):
                break
                    
        #return count                
              
        #print(count)
        if(count > 0):
            for i in range(count+1):
                #print(i)
                if(i != count):
                    s +=strs[0][i]
            return s
            
        else:
            return s
        
        
obj = Solution()

print(obj.longestCommonPrefix(["ssdfff","dsdfs","ss"]))