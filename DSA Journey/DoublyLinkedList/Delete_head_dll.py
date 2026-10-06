class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        # Your code goes here
        if head is None:
            return None
        head = head.next
        if head is not None:
            head.prev = None
        return head