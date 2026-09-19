class Solution:
    def postorder(self, root):
        ans = []
        def solve(root):
            if root is None:
                return ans
            else:
                solve(root.left)
                solve(root.right)
                ans.append(root.data)
        solve(root)
        return ans