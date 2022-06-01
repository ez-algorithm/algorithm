from collections import defaultdict


def solution(record):
    answer = []

    nicknames = defaultdict()
    for r in record:
        r = r.split()

        if r[0] == "Enter":
            nicknames[r[1]] = r[2]
            answer.append([r[0], r[1]])
        elif r[0] == "Leave":
            answer.append([r[0], r[1]])
        else:
            nicknames[r[1]] = r[2]

    for idx, a in enumerate(answer):
        if a[0] == "Enter":
            answer[idx] = f"{nicknames[a[1]]}님이 들어왔습니다."
        else:
            answer[idx] = f"{nicknames[a[1]]}님이 나갔습니다."

    return answer
