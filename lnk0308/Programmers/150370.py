def solution(today, terms, privacies):
    answer = []    
    
    #개인정보 탐색 
    for num in range(len(privacies)):
        privacy = privacies[num]
        
        # 개인정보 수집일자, 약관 종류 
        # 공백 기준으로 split하여 분리 후, 값 얻기  
        date = privacy.split()[0]
        pri_type = privacy.split()[1]
        
        # 약관 종류에 따른 유효기간 얻기 
        valid_term = 0 # 유효기간 변수 
        for term in terms:
            temp_type = term.split()[0]
            if pri_type == temp_type:
                valid_term = term.split()[1]
                break # 수많은 약관 종류 중, 찾고자 하는 약관종류를 찾았을 시 바로 탈출 
                
        # 유효기간은 최대 100달까지 가능
        # 유효기간을 년월로 환산 
        valid_year = int(int(valid_term) / 12)
        valid_month = int(valid_term) % 12        
        
        # 개인정보 수집일자에 유효기간 더하기 (월 먼저) 
        valid_month += int(date[5:7])
        
        # 유효기간을 더했을 때 달이 12월을 넘어간 경우 처리 
        # 년+1, 나머지가 월이 됨 
        if valid_month > 12:
            valid_year += (int(date[0:4]) + int(valid_month / 12))
            valid_month %= 12
        else: 
            valid_year += int(date[0:4])
        
        
        # 계산된 유효기간 년월을 통해 파기 정보 탐색 
        if int(today[0:4]) > valid_year: # 년도 비교 / 유효기간 년도가 이미 과거라면 파기 대상 
            answer.append(num+1)
        elif int(today[0:4]) == valid_year and int(today[5:7]) > valid_month: # 년월 비교 / 년도는 같아도 월이 과거라면 파기 대상 
            answer.append(num+1)
        elif int(today[0:4]) == valid_year and int(today[5:7]) == valid_month and int(today[8:]) >= int(date[8:]): # 년월일 비교 
            answer.append(num+1)
                    
    # 파기대상 개인정보 번호를 오름차순으로 정렬             
    answer.sort()        
    return answer