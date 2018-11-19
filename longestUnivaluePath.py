class Solution(object):
    def longestUnivaluePath(self, root):
        self.longest = 0
        
        def node_length(node):
            if node == None: 
                return 0
            if node.left == None and node.right == None:
                return 0
            
            left_length = node_length(node.left)
            right_length = node_length(node.right)

            

            if node.left and node.right and node.left.val == node.val and node.right.val == node.val:
                if left_length + right_length + 2 > self.longest:
                    self.longest = left_length + right_length + 2
                return max(left_length, right_length) + 1
            if node.left and node.left.val == node.val:
                left_length += 1
                if left_length > self.longest:
                    self.longest = left_length
                return left_length
                
            if node.right and node.right.val == node.val:
                right_length += 1
                if right_length > self.longest:
                    self.longest = right_length
                return right_length
            return 0

            
            
            
            







        node_length(root)
        return self.longest
