class Solution:
    def levelOrder(self, root):
        ans=[]
        if root is None:
            return ans
        queue = [root]

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                root = queue.pop(0)
                level.append(root.data)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(level)
        return ans