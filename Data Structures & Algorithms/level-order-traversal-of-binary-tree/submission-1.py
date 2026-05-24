# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        # BFS
        q = deque([(0, root)])
        res = []
        cur_level = -1
        while q:
            l, node = q.popleft()
            if not node:
                continue
            elif l == cur_level:
                res[-1].append(node.val)
            else: # l > cur_level
                res.append([node.val])
            cur_level = l
            q.append((l + 1, node.left))
            q.append((l + 1, node.right))
        return res