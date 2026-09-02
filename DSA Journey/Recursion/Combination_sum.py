class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        curr = []

        def solve(index, total):

            if total == target:
                ans.append(curr[:])
                return

            if total > target or index == len(candidates):
                return

            curr.append(candidates[index])
            solve(index, total + candidates[index])
            curr.pop()

            solve(index + 1, total)

        solve(0, 0)
        return ans