# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

class Solution:
    def reverseDLL(self, head):
        # Your code goes here
        curr = head
        new = None

        while curr:
            nextNode = curr.next

            curr.next = curr.prev
            curr.prev = nextNode

            new = curr
            curr = nextNode

        return new