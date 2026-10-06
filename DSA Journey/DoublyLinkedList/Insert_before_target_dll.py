
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeGivenNode(self, node: ListNode, X: int) -> None:
        new = ListNode(X)

        new.prev = node.prev
        new.next = node

        if node.prev:
            node.prev.next = new

        node.prev = new