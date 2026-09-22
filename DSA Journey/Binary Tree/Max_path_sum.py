class Solution:
    def maxPathSum(self, root):
        maxsum = float('-inf')
        def solve(root):
            nonlocal maxsum
            if root is None:
                return 0
            else:
                left = max(0,solve(root.left))
                right = max(0,solve(root.right))
            currsum = left+root.val+right
            maxsum = max(maxsum,currsum)
            return root.val+ max(left,right)
        solve(root)
        return maxsum                