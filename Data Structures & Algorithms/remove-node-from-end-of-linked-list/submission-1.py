# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Reverse node
        # Iterate the node with counting from the tail to the head.
        # During the iteration, reverse again the edge
        # Revove i-th node from the tail
        
        # Reverse Node
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        tail = prev

        # Iterate from the tail
        prev = None
        cur = tail
        count = 1
        while cur:
            if count == n:
                # Remove the current node
                cur = cur.next
            else:
                # Reverse again the list
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            count += 1
        # return the cur
        return prev