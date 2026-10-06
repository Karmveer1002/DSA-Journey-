
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteKthElement(self, head: ListNode, k: int) -> ListNode:
        
        curr = head 

        for i in range(k-1):
            curr = curr.next
        if curr == head:
            head = head.next
            if head is not None:
                head.prev = None
            return head
        curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        return head
            