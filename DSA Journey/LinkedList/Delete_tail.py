class Solution:
    def deleteTail(self, head):
        if head is None:
            return None
        if head.next is None:
            return None
        curr = head
        if curr == head:
            while curr.next.next is not None:
                curr = curr.next
        curr.next = None
        return head
