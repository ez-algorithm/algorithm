def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            recon = s[i:j]
            if recon == recon[::-1]:
                answer = max(answer, len(recon))

    return answer