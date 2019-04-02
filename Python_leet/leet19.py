# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        count = 1
        while current.next:
            count +=1
            current = current.next
        new = head
        if(count > 1):
            diff = count - n
            if diff == 0:
                head = new.next
            else:
                while diff>1:
                    diff -=1
                    new = new.next
                #print()
                new.next  = new.next.next
        else:
            head = None        
        return head