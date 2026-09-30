class Solution:
    def isBST(self, root):
        def check(root, min, max):
            if root is None:
                return True

            if root.data <= min or root.data >= max:
                return False

            left = check(root.left, min, root.data)
            right = check(root.right, root.data, max)

            return left and right

        return check(root, float('-inf'), float('inf'))