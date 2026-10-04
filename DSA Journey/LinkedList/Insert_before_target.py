class ListNode:
  def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def insertBeforeX(self, head, X, val):
        if head == None:
            return None
        new = ListNode(val)

        if head.data == X:
            new.next = head
            return new

        prev = None
        curr = head

        while curr != None:
            if curr.data == X:
                new.next = curr
                prev.next =  new
                return head
            prev = curr
            curr = curr.next
        return head