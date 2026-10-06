
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Solution:
    def arrayToDoublyLinkedList(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        curr = head

        for i in range(1, len(arr)):
            new = ListNode(arr[i])

            curr.next = new
            new.prev = curr

            curr = new

        return head