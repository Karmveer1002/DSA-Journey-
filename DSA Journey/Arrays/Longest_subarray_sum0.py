class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        max_length = 0
        hash_map = {0: -1}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum in hash_map:
                length = i - hash_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                hash_map[prefix_sum] = i

        return max_length