class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #print(type(a))
        #a1 = a.split()
        inta = 0
        intb = 0
        #print(a)
		# reversing the string so that when we supply 1010 it should not read 101 as it take msb as first letter
        a1 = a[::-1]
        b1 = b[::-1]
        #print(a1)
        for i in range(len(a)):
            
            if a1[i] == '1':
                #print(i)
                inta += 2**i
            else:
                continue
        #print(inta)
        for j in range(len(b)):
            #print(b[j)
            if b1[j] =='1':
                intb += 2**j
            else:
                continue
        #print(intb)
        #return intb
         
        total = inta + intb
        bin_total = "{0:b}".format(total)
        return str(bin_total)
        
x = Solution()
print(x.addBinary('1010','1011'))