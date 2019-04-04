# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        nextitem = head
        prev = None
        while current:
            nextitem = nextitem.next
            current.next = prev
            prev = current
            current = nextitem
            
        #head =  current
        current = prev
        return current
           
    '''
	def reverseList(self, head: ListNode) -> ListNode:
        current = head
        nextitem = head
        prev = None
        def recurse(current):
            if(current.next == None):
                return prev 
            else:
                nextitem = nextitem.next
                prev = current
                current.next = prev
            #current = nextitem
            recurse(current = nextitem)
        #current = prev
        return current
		'''