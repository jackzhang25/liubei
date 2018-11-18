class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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
