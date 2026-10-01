class Solution:
    def deleteNodeWithValueX(self, head, X):
        if head is None:
            return None
        if head.data == X:
            return head.next
        prev = None
        curr = head

        while curr:
            if curr.data ==X:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        return head