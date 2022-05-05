class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        stop = False
        result = ""
        min_len = 987654321
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
                
        for i in range(min_len):
            x = ''
            for j in range(1, len(strs)):
                str = strs[j]
                str_bf = strs[j-1]
                x = str[i]
                if x != str_bf[i]:
                    stop = True
                    break
            if stop:
                break
            else:
                result += x
        return result
        
        """
        :type strs: List[str]
        :rtype: str
        """
        
