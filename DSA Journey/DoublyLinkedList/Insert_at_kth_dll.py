
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeKthPosition(self, head: ListNode, X: int, K: int) -> ListNode:
        new = ListNode(X)

        if K == 1:
            new.next = head
            if head is not None:
                head.prev = new
                head = new
            return head
        curr = head
        for i in range(K-1):
            curr = curr.next
        new.prev = curr.prev
        new.next = curr
        curr.prev.next = new
        curr.prev = new
        return head