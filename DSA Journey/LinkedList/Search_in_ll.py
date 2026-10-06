"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
        
class Solution:
    def searchKey(self, head, key):
        curr = head 
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False