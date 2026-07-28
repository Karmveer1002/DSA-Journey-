class Solution:
    def largest(self, arr):
        lar = 0
        i = int()
        for i in arr:
            if i>=lar:
                lar = i
            
        return lar