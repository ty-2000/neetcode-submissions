# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        r = preorder[0] # 3
        tn = TreeNode(r)
        # Find tn.val in the inorder list
        i = inorder.index(r) # 0
        tn.left = self.buildTree(preorder[1:1+i], inorder[:i]) # ([], [])
        tn.right = self.buildTree(preorder[1+i:], inorder[i+1:]) # ([3,4], [3,4]) ([4], [4])
        return tn