class Solution:
    def tree_traversal(self, root):
        
        In = []
        Pre = []
        Post = []

        def solve(root):
            if root is None:
                return 
            
            Pre.append(root.data)

            solve(root.left)

            In.append(root.data)

            solve(root.right)

            Post.append(root.data)

        solve(root)   
        return[In,Pre,Post]

