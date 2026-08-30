class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        def count(index,Sum):
            if index == len(nums):
                if Sum  == k:
                    return 1
                else:
                    return 0
            take = count(index+1,Sum+nums[index])
            not_take = count(index+1, Sum)

            return take+not_take
        return count(0,0)