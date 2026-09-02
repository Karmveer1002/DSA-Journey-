class Solution:
    def subsetSums(self, nums):
        ans = []
        def solve(index,total):
            if index == len(nums):
                ans.append(total)
                return()
            
            take = solve(index+1,total+nums[index])

            not_take = solve(index+1,total)

        solve(0,0)
        return ans