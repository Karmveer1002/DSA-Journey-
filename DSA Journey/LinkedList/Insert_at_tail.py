class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def insertAtTail(self, head, X):
        new = ListNode(X)
        if head == None:
            return new

        curr = head
        
        while curr.next != None:
            curr = curr.next
        curr.next = new
        return head