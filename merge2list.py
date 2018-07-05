# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        
        
        for i in range(len(l1)+1):
            flag = 0
            flag2 = 0
            #print(i)
            for j in range(len(l2)):
                #print(j)
                if(l2[j] == 'X'):
                    continue
                else:
                    
                    if (l1[i] < l2[j]):
                        flag += 1
                        if(flag == 1):
                            l3.append(l1[i])
                            print("l1:-",l3)
                    elif (l1[i] == l2[j]):
                        l3.append(l1[i])
                        #l3.append(l2[j])
                        l2.pop(j)
                        l2.insert(0,"X")
                    else:
                        flag2 +=1
                        if(flag2 == 1):
                            l3.append(l2[j])
                            l2.pop(j)
                            l2.insert(0,"X")
                            #print("length",len(l2))
                            #mad -=1
                            
                            print("l2:-",l3)
                       
        print(l2)
        flag3 =0
        for k in range (len(l2)):
            
            if (l2[j] !='X'):
                flag3 +=1
                if(flag3==1):
                    l3.append(l2[j])
            else:
                continue
        return l3
        
x = Solution()
print(x.mergeTwoLists([1,2,4,4,5] , [1,3,4,4,5]))