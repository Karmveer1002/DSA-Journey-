"Approach 1"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            #odd
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if right - left+1 > len(longest):
                    longest = s[left:right+1]
                    left-=1
                    right+=1
            #even
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if right - left+1 > len(longest):
                    longest = s[left:right+1]
                    left-=1
                    right+=1
        return longest

"Approach 2"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):

            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1

        return s[start:start + max_len]