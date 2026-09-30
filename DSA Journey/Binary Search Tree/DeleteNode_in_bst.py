class Solution:
    def deleteNode(self, root, key):

        if root is None:
            return None

        if key < root.data:
            root.left = self.deleteNode(root.left, key)

        elif key > root.data:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            successor = root.right

            while successor.left:
                successor = successor.left

            root.data = successor.data

            root.right = self.deleteNode(root.right, successor.data)

        return root