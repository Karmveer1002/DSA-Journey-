class Solution:
    def deleteHead(self, head):
        curr = head
        if head is None:
            return head
        
        head = head.next
        return head