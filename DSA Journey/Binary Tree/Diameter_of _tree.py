class Solution:
    def diameterOfBinaryTree(self, root):
        self.dia = 0

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            self.dia = max(self.dia, left + right)

            return 1 + max(left, right)

        height(root)
        return self.dia