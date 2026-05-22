# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # s, t as min(p, q), max(p, q)
        # s <= ans <= t
        # Iterate from the root node
        # If the current node is smaller than s -> cur = cur.right
        # If the current node is larger than t  -> cur = cur.left
        

        s = min([p, q], key=lambda x: x.val)
        t = max([p, q], key=lambda x: x.val)

        cur = root
        while cur != s and cur != t:
            if cur.val < s.val:
                cur = cur.right
            elif cur.val > t.val:
                cur = cur.left
            else:
                break
        return cur