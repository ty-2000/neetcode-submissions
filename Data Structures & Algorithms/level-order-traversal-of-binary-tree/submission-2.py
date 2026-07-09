# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res = []
        q = deque([root])
        
        while q:
            tmp = [] # node values at the level so far
            l = len(q)
            for _ in range(l):
                e = q.popleft()
                tmp.append(e.val)
                if e.left: q.append(e.left)
                if e.right: q.append(e.right) # [4, 5, 6, 7]
            res.append(tmp)
        return res
                