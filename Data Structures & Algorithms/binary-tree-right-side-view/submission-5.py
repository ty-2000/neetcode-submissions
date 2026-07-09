# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(tn: TreeNode, depth: int) -> None:
            if tn is None:
                return
            # Update the res
            if len(res) == depth: # [1]
                res.append(tn.val)
            else:
                # The current value is the most right position so far
                res[depth] = tn.val
            # Visit left
            dfs(tn.left, depth + 1)
            # Visit right
            dfs(tn.right, depth + 1)
        
        dfs(root, 0)
        return res