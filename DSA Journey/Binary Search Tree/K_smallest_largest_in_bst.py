class Solution:
    def kLargestSmall(self, root, k):
        small = []
        large = []
        def inorder(root):
            if root is None:
                return None
            else:
                inorder(root.left)
                small.append(root.data)
                inorder(root.right)
        def rev(root):
            if root is None:
                return None
            else:
                rev(root.right)
                large.append(root.data)
                rev(root.left)
            
        inorder(root)
        rev(root)
        return [small[k-1],large[k-1]]