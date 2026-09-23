class Solution:
    def unique_binary_tree(self, a, b):
        if a==b:
            return False
        if a==2 or b==2:
            return True 
            
        return False