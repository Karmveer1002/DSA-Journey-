class Solution:
    def longestCommonPrefix(self, strs):
        pre = strs[0]
        for str in strs[1:]:
            while not str.startswith(pre):
                pre = pre[:-1]
                if pre == "":
                    return ""
        return pre