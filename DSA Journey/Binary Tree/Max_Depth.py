class Solution:
    def maxDepth(self , root):
        if root is None:
            return 0
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
        
        return 1+ max(leftdepth,rightdepth)