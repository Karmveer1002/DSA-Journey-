
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteGivenNode(self, node: ListNode) -> None:
        # Your code goes here
        curr = node
        curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        