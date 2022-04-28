def solution(n, words):
    
    round = 0
    prev_word = words[0][0]
    
    for i in range(len(words)):
        #모든 사람만큼 돌았다면 다음 차례 게임이 시작됨
        if i%n == 0:
            round += 1
        #이미 말한 단어 or 이전 단어의 마지막 알파벳에 맞지 않은 단어면 탈락
        if words[i] in words[:i] or prev_word[-1] != words[i][0]:
            return [i%n+1, round]
        
        prev_word = words[i]

    #아무도 탈락하지 않았다면 기본값 반환
    return [0, 0]