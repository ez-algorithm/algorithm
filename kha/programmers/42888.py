def solution(record):
    
    uid_dict = {}
    answer = []
    
    #최종 uid 구하기
    for item in record:
        parse_list = list(map(str, item.split()))
        if parse_list[0] != "Leave":
            uid_dict[parse_list[1]] = parse_list[2]
            
    #출력할 메세지 생성하기
    for item in record:
        parse_list = list(map(str, item.split()))
        if parse_list[0] == "Enter":
            answer.append(uid_dict[parse_list[1]]+"님이 들어왔습니다.")
        elif parse_list[0] == "Leave":
            answer.append(uid_dict[parse_list[1]]+"님이 나갔습니다.")
    
    return answer