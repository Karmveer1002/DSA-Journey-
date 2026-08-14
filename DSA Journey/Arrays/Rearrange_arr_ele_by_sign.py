class Solution:
    def rearrangeArray(self, nums):
        ans=[0]*len(nums)
        p = 0
        n = 1
        for i in range (0,len(nums)):
            if nums[i]>0:
                ans[p] = nums[i]
                p = p+2
            else:
                ans[n] = nums[i]
                n = n+2
        return ans