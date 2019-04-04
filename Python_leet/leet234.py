# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        new = head
        stack = []
        while current:
            #count +=1
            stack.append(current.val)
            current =  current.next
            
        stack.reverse()
        count  = 0
        #print(stack)
        for i in stack:
            if(i == new.val):
                new = new.next
                count +=1
        if(count == len(stack)):
            return True
        
        return False
            
        