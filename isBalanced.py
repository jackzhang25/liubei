# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1
    
    def isBalanced(self, root):
        if root == None:
            return True
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left - right > 1 or right - left > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
