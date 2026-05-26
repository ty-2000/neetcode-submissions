# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2:  ListNode | None) ->  ListNode | None:
        if l1.val == 0: return l2
        elif l2.val == 0: return l1

        l_root = ListNode()
        cur1, cur2 = l1, l2
        cur = l_root
        c = 0

        while cur1 or cur2:
            # calculate the sum of values and the carried val (0 or 1)
            # If any of cur is null, treat it as zero

            # store the first digit of the sum into a new node
            # set carry one if the sum is equal or greater than 10
            # move cur1 and cur2 forward by one

            # Calculate sum of the values including a carried value
            val = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0) + c

            # Calculate the carried value
            if val >= 10:
                c = 1
                val %= 10
            else:
                c = 0
            
            # Create a new node
            cur.next = ListNode(val)
            cur = cur.next

            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next

        if c:
            cur.next = ListNode(c)
        
        return l_root.next