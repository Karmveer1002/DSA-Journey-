class Solution:
    def largeOddNum(self, num):
        arr = str(num)

        for i in range(len(arr) - 1, -1, -1):
            if int(arr[i]) % 2 != 0:
                ans = arr[:i + 1]

                j = 0
                while j < len(ans) and ans[j] == '0':
                    j += 1

                return ans[j:]

        return ""