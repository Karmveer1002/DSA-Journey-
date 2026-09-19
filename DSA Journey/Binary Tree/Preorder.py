class Solution:
    def preorder(self, root):
        ans =[]
        def solve(root):
            if root is None:
                return ans
            else:
                ans.append(root.data)
                solve(root.left)
                solve(root.right)
        solve(root)
        return ans