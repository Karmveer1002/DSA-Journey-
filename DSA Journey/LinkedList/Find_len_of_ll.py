class Solution:
    def getLength(self, head):
        
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        return count