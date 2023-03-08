from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    dt = {k: int(v) for k, v in map(lambda t: t.split(' '), terms)}
    today = datetime.strptime(today, '%Y.%m.%d')
    for idx, privacy in enumerate(privacies):
        sd, t = privacy.split(' ')

        y, m, d = map(int, sd.split('.'))
        m += dt[t]
        y += m // 12
        m = m % 12
        
        if m % 12 ==0:
            y -= 1
            m = 12

        if today >= datetime(y, m, d):
            answer.append(idx + 1)
    return answer