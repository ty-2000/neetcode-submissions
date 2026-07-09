# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tn: TreeNode, max_allowance: int, min_allowance: int) -> bool:
            if tn is None: return True
            if tn.val >= max_allowance or tn.val <= min_allowance: return False
            # Left traverse
            # Right traverse
            return dfs(tn.left, tn.val, min_allowance) and dfs(tn.right, max_allowance, tn.val)
        return dfs(root, float('inf'), float('-inf'))