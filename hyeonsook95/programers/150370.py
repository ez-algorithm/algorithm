def solution(today, terms, privacies):
    answer = []
    
    dt = {k: int(v) for k, v in map(lambda t: t.split(' '), terms)}
    for idx, privacy in enumerate(privacies):
        sd, t = privacy.split(' ')

        y, m, d = map(int, sd.split('.'))
        dm = m + dt[t]
        y += dm // 12
        m = dm % 12
        
        if m == 0:
            y -= 1
            m = 12

        if today >= f"{y}.{str(m).zfill(2)}.{str(d).zfill(2)}":
            answer.append(idx + 1)
    return answer