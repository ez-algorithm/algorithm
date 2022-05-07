class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #문자열의 길이대로 정렬
        strs.sort(key=len)
        
        base_word = strs[0]
        
        answer = ""
        
        for i in range(len(base_word)):
            is_finish = True
            for word in strs:
                if word[i] != base_word[i]:
                    is_finish = False
            #모든 문자열에 해당 문자가 있으면 접두사에 포함되는 문자임
            if is_finish:
                answer += base_word[i]
            else:
                break
        
        return answer
            