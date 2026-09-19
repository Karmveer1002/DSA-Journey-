class Solution:
    def inorder(self, root):
        #your code goes here
        ans=[]
        def solve(root):
            if root is None:
                return ans
            else:
                solve(root.left)
                ans.append(root.data)
                solve(root.right)
        solve(root)
        return ans