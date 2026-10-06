
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeTail(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        
        new  = ListNode(X)
        if head is None:
            return new
        if head.next is None:
            new.next = head
            head.prev = new
            return new
        curr = head

        
        while curr.next is not None:
            curr = curr.next
        new.prev = curr.prev
        new.next = curr
        curr.prev.next = new
        curr.prev = new
        return head
