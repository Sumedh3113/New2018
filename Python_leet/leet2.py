# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 1
        linksum1 , linksum2 = 0, 0
        while l1 and l2:
            linksum1 += l1.val*i 
            
            linksum2 += l2.val*i
            
            i *= 10 
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            linksum1 +=l1.val*i
            i *=10
            l1 = l1.next
        while l2:
            linksum2 += l2.val*i
            i *=10
            l2 = l2.next
        
        sum3 =  linksum1 + linksum2
        
        l3 = ListNode(sum3%10)
        
        head =  l3
        
        final = sum3//10
        
        while final:
            l3.next = ListNode(final%10)
            l3 =  l3.next 
            final = final//10
            
            
        
        
        return head
        