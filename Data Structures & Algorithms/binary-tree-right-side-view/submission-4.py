# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # Always right element is prioritized
        #
        # DFS with left-fist way
        # Initialize the list for storing the data of the node value
        # At the tree search, store the element at its depth-index. If already a element at the index, update it.

        res = []
        def dfs(node: TreeNode | None, depth):
            # if None, return
            if node is None: return

            # Store own value
            if len(res) <= depth:
                res.append(node.val)
            else:
                res[depth] = node.val
            
            # Search from the left node
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res