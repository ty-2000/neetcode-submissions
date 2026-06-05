# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS by in-order (left first, self, right)
        
        cnt = 0 # Count from the smallest
        res = root.val

        def dfs(n: TreeNode) -> int:
            nonlocal cnt
            nonlocal res
            
            if n is None: return 

            # Left first
            dfs(n.left)
            if cnt == k:
                return
            cnt += 1
            if cnt == k:
                res = n.val
                return
            
            dfs(n.right)
        
        dfs(root)
        return res