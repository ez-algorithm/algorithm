def solution(s):
    answer = ''
    changed = True

    # 카멜 스타일로 바꿔라.
    # 주의점: 공백 문자가 연속해서 나올 수 있는데 이 경우 공백을 그대로 출력해줘야 한다.
    for char in s:
        if char == ' ':
            answer += char
            changed = True
        elif changed:
            answer += char.upper()
            changed = False
        else:
            answer += char.lower()

    return answer