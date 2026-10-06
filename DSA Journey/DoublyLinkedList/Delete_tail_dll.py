class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteTail(self, head: ListNode) -> ListNode:
        # Your code goes here
        if head is None:
            return None
        if head.next is None:
            return None

        curr = head
        
        while curr.next != None:
            curr = curr.next
        curr = curr.prev
        curr.next = None

        return head
