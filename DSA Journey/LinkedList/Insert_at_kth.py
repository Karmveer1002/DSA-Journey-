class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, k):
        

        new = ListNode(X)

        if k == 1:
            new.next = head
            return new
        
        prev = None
        curr = head

        for i in range(k-1):
            prev = curr
            curr = curr.next
        new.next = curr
        prev.next = new
        return head