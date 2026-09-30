
class Solution:
    def floorCeilOfBST(self, root, key):
        floor = -1
        ceil = -1
        
        while root:
            if root.data == key:
                floor = key
                ceil = key
                break
            if root.data < key:
                floor = root.data
                root = root.right
            else:
                ceil = root.data
                root = root.left
        return[floor,ceil]