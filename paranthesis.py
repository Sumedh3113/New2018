class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        status = False
        bracket = []
        
        if (s == ""):
                return True
		# appending white space at the end so that we can access the last element using loop till len(s)-1		
        s +=" "        
        for i in range(len(s)-1):
                
            #if( i < len(s)):
            if( s[i] =="("):
                if(s[i+1]==")"):
                    status = True
                else:
                    bracket.append(s[i])
                    
            if( s[i] =="{"):
                if(s[i+1]=="}"):
                    status = True
                    
                else:
                    bracket.append(s[i])
                    
            if( s[i] =="["):
                if(s[i+1]=="]"):
                    status = True
                    
                else:
                    bracket.append(s[i])
            
            if(bracket != []):
                
                x = bracket[-1]
            
            if(s[i+1] == ")"):
                #print("hello")
                if( x == "(" ):
                    #print("Hi")
                    bracket.pop()
                    if(bracket == []):
                        status = True
                    else:
                        pass
                        
                    
            if(s[i+1] == "}"):
                if( x == '{'):
                    bracket.pop()
                    if(bracket == []):
                        status = True
                    else:
                        pass
                    
            if(s[i+1] == "]"):
                if( x == '['):
                    bracket.pop()
                    if(bracket == []):
                        status = True
                    else:
                        pass
                    
            '''
            if(i == len(s)-1):
                
                if(s[i+1] == '(' or s[i+1] == '{' or s[i+1] == '['or s[i+1] == ']' or s[i+1] == '}' or s[i+1] == ')' ):
                    
                    bracket.append(s[i+1])
            '''
    
        print(bracket)    
        if(bracket == [] and status):    
            return status
        else:
            return False
        
        
obj = Solution()
print(obj.isValid("([])[{}]"))