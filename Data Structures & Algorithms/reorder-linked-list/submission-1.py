# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        # Find the center point
        # Reverse from the center point to the last
        # Two pointers at the first and last positions, begin the iteration at the same time
        # Move the node at the right pointer to the next of the left pointer

        # Find the center
        h = t = head
        while h and h.next:
            t = t.next
            h = h.next
            h = h.next if h else None
        print('found center: ', t.val)

        # Reverse from t to h
        prev = None
        cur = t
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        print('reversed')        

        # Iterate from the both side
        l, r = head, prev
        while l and r:
            # o -> o <- o
            # o -> o 
            if l == r or l.next == r: break
            l_next = l.next
            r_next = r.next
            l.next = r
            r.next = l_next
            r = r_next
            l = l_next