# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            
        def dfs(n: TreeNode, max_so_far: int):
            cnt = 0
            # Compare the current value and max_so_far
            next_max_so_far = max(n.val, max_so_far)
            
            # If val < max_so_far: NOT Good
            # Continue the traversal
            
            # If val >= max_so_far: Good
            # Add the current node to the result
            # Update the max_so_far, and continue the traversal
            
            if n.val == next_max_so_far:
                cnt += 1
            
            if n.left:
                cnt += dfs(n.left, next_max_so_far)
            
            if n.right:
                cnt += dfs(n.right, next_max_so_far)
            return cnt
        
        return dfs(root, float('-inf'))
