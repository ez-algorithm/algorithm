def solution(s):
    answer = ''
    
    flag = False # 단어의 첫 문자를 발견했는지 여부를 나타내는 flag 변수 
    
    # 문자열을 index로 탐색 
    for idx in range(len(s)):
        
        # 단어의 첫 문자를 이미 만난 상태라면
        if flag == True:
            # 공백이 아닌 대문자 알파벳을 만나면, 소문자로 변경하여 넣기 
            if s[idx].isupper() == True and s[idx] != ' ':
                answer+=s[idx].lower()
            # 공백을 만나면 공백을 답에 넣고, 단어가 끝났으니 단어의 첫문자를 찾는 flag 변수 초기화  
            elif s[idx] == ' ':
                flag = False
                answer+=s[idx]
            # 공백이 아닌 소문자는 바로 답에 넣기     
            else:
                answer+=s[idx]
        # 단어의 첫 문자가 공백이 아닐 땐, 대문자로 변경 후 답에 넣고 첫문자 찾았으니 flag값 변경          
        elif s[idx] != ' ':
            flag =True
            answer+=s[idx].upper()
        # 단어의 첫 문자를 못찾은 상태에서 공백을 만나면, 그냥 그대로 공백만 답에 넣기     
        else:
            answer+=s[idx]
            
    return answer