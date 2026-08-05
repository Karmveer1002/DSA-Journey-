# Approach 1 : Hashmap
class Solution:
    def majorityElement(self, nums):
        hashmap = {}
        count = 0
        n = len(nums)
        for i in range (nums[0],n):
            if nums[i] == i:
                count+=1
        if count > n/2:
            return nums[i]

# Approach 2 : Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for i in range(len(nums)):
            curr = nums[i]
            if count==0:
                candidate = curr
                count=1
            elif curr == candidate:
                count+=1
            else:
                count-=1
        return candidate