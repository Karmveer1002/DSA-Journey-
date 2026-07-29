class Solution:
    def leaders(self, nums):
        current_max = nums[len(nums)-1]
        leaders = [current_max]
        for i in range(len(nums)-1,-1,-1):
            current_element = nums[i]
            if current_element > current_max:
                current_max = current_element
                leaders.append(current_element)
        leaders.reverse()
        return leaders