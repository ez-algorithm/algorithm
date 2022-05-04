class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = [a for a in strs[0]]
        result = ""
        print(answer)
        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                if answer[j] != strs[i][j]:
                    result = ''.join(answer[:j])
                    return result
        return answer