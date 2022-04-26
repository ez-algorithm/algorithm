import collections
def solution(n, words):
    answer = [0,0]
    last_words = [''] * n #각 사람의 마지막 단어 저장
    l = len(words)
    cnt = 1
    d = collections.defaultdict()
    d[words[0]] = 1
    last_words[0] = words[0]
    
    for i in range(1,l):
        w = words[i]
        j = i%n
        last_words[j] = w
        
        # 차례
        if j == 0:
            cnt += 1
        if len(w) == 1:
            answer[0] = j+1
            answer[1] = cnt
            break
        # 이전에 나온 단어인지 확인
        if w in d:
            answer[0] = j+1
            answer[1] = cnt
            break          
        else:
            d[w] = 1
                   
        # 이전 사람의 단어 끝말확인
        tmp = ''
        if j == 0:
            tmp = last_words[n-1]
        else:
            tmp = last_words[j-1]
        #print(i, j, tmp, tmp[-1])
        if tmp[-1] != w[0]:
            answer[0], answer[1] = j+1, cnt
            break

    return answer
