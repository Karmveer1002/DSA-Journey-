class Solution:
    def quickSort(self, nums):

        if len(nums) <= 1:
            return nums

        pivot = nums[0]

        left = []
        right = []

        for i in range(1, len(nums)):

            if nums[i] <= pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        return self.quickSort(left) + [pivot] + self.quickSort(right)