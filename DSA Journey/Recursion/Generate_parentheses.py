class Solution:
    def generateParenthesis(self, n):
        ans = []
        curr=[]
        def solve(Open,Close):
            if Open == n and Close == n:
                ans.append("".join(curr))
                return 
            #Open
            if Open < n:
                curr.append("(")
                solve(Open+1,Close)
                curr.pop()

            #Close
            if Close < Open:
                curr.append(")")
                solve(Open,Close+1)
                curr.pop()
        solve(0,0)
        return ans