'''
@author : Chandu Soman
'''
Class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        i = 0
        j = 0

        if len(l1) < len(l2):
        	n = len(l1)
        else:
        	n = len(l2)

        for _ in range(len(l1)+ len(l2)): 

        	if i >= len(l1) or j >= len(l2):
        		break

        	if l1[i] == l2[j]:
        		l3.append(l1[i])
        		i += 1
        	elif l1[i] < l2[j]:
        		l3.append(l1[i])
        		i += 1
        	else:
        		l3.append(l2[j])
        		j += 1

        if i >= len(l1):
        	l3.extend(l2[j:])
        if j >= len(l2):
        	l3.extend(l1[i:])

        return l3