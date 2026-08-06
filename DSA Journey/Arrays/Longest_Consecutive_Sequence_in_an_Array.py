class Solution:
    def longestConsecutive(self, nums):
        hashset = set(nums)
        max_length = 0
        for num in nums:
            if num-1 not in hashset:
                curr=num
                length=1
                while curr+1 in hashset:
                    curr +=1
                    length +=1
                max_length = max(max_length,length)
        return max_length