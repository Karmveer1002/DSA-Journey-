class Solution:
    def LLTraversal(self, head):
        ans = []
        curr = head
        while curr:
            ans.append(curr.data)
            curr = curr.next
        return ans