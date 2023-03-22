def solution(s):
    answer = "" 
    number ={'zero': '0', 'one': '1', 'two': '2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 
             'eight':'8', 'nine':'9'} # 영문과 숫자를 매칭 해놓은 딕셔너리 
    
    check="" # 숫자를 의미하는 각 알파벳을 담을 check 변수  
    
    # 주어진 s문자열 탐색
    for idx in range(len(s)):
        # 숫자를 만나면, 바로 정답에 넣기 
        if s[idx].isdigit() == True:
            answer+=s[idx]
        # 알파벳을 만나면 check 변수에 넣기     
        else:
            check+=s[idx]
        
        # 각 알파벳의 조합이 숫자를 의미하도록 완성되었는지를 확인 
        # 숫자를 의미하면, 정답에 넣고 check 변수 초기화 
        if check in number:
            answer+= number[check]
            check=""    
    
    # 숫자를 반환해야 하기 때문에, int형으로 형변환 
    return int(answer)