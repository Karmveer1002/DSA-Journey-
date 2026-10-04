class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next
class Solution:
    def insertAtHead(self, head, X):
        new = ListNode(X)
        new.next = head
        head = new
        return head 