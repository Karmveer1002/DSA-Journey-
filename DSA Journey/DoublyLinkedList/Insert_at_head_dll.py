
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        new = ListNode(X)
        if head is not None:
            new.next = head
            head.prev = new
        head = new
        return head