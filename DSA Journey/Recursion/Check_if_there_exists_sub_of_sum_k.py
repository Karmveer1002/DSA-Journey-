class Solution:
    def checkSubsequenceSum(self, nums, k):

        def solve(i, total):
            if total == k:
                return True

            if i == len(nums) or total > k:
                return False

            
            if solve(i + 1, total + nums[i]):
                return True

            
            return solve(i + 1, total)

        return solve(0, 0)
