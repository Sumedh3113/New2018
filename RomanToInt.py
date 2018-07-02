class Solution:
    def romanToInt(self, s):
        """
        :type i: itr
        :rtype: int
        """
        #x = liit(i)
        #
        x = 0
        #lst =list(s)
        #print(lst)
        ''' I can be placed before V (5) and X (10) to make 4 and 9
        X can be placed before L (50) and C (100) to make 40 and 90.        
        C can be placed before D (500) and M (1000) to make 400 and 900.'''
        #for i in lst:
        for i in range(len(s)):
            #print(s[i])
                
                
            if(s[i] == 'I'):
                if(i != len(s)-1):    
                    if(s[i+1]=='V'):
                        x -=1
                            
                    elif(s[i+1]=='X'):
                        x -=1
                            
                    else:
                        x += 1
                else:
                        x += 1
                    
            if(s[i]== 'V'):
                x += 5
                     
                
            if(s[i] == 'X'):
                
                if(i != len(s)-1):    
                    if(s[i+1] == 'L'):
                        x -=10
                        
                    elif(s[i+1] == 'C'):
                        x -=10
                        
                    else:
                        x += 10
                else:
                    x +=10
                    
            if(s[i]== 'L'):
                x +=50 
                    
            if(s[i]== 'C'):
                
                if(i != len(s)-1):    
                    if(s[i+1] == 'D'):
                        x -= 100
                        
                    elif(s[i+1] == 'M'):
                        x -= 100
                    
                    else:
                        x +=100
                else:
                    x +=100
                    
            if(s[i]== 'D'):
                x +=500 
                
            if(s[i]== 'M'):
                x +=1000
                
        return x

object1 = Solution()
print(object1.romanToInt('IXIVIC'))