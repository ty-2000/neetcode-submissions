# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(n: TreeNode, rng: tuple[int, int]) -> bool:
            if n is None: return True
            if not (rng[0] < n.val < rng[1]):
                return False
            return all([dfs(n.left, (rng[0], n.val)), dfs(n.right, (n.val, rng[1]))])
        
        return dfs(root, (-float('inf'), float('inf')))