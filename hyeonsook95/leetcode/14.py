class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        start, end = 0, len(prefix)

        for chars in strs[1:]:
            while prefix and prefix != chars[start:end]:
                end -= 1
                prefix = prefix[start:end]
            if not prefix:
                return prefix

        return prefix
