# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(tn: TreeNode, max_so_far: int) -> None:
            nonlocal cnt
            if tn.val >= max_so_far:
                # Good Node
                cnt += 1
                max_so_far = tn.val
            if tn.left: dfs(tn.left, max_so_far)
            if tn.right: dfs(tn.right, max_so_far)
            return
        dfs(root, float('-inf'))
        return cnt