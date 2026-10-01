class Solution:
    def deleteKthNode(self, head, k):
        if head is None:
            return None

        if k == 1:
            return head.next

        curr = head
        prev = None

        for i in range(k - 1):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head