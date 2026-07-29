class Solution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range (1,len(nums)):
            curr_ele = nums[i] 
            curr_sum = max(curr_sum + curr_ele , curr_ele)
            if curr_sum > max_sum:
                max_sum=curr_sum
        
        return max_sum