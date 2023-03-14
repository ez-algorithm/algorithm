from itertools import combinations
from collections import Counter

def solution():
    basic_alpha = set('antatica')

    n, k = map(int, input().split())
    
    k -= len(basic_alpha)

    words = []
    alpha = set()
    alpha_count = Counter()
    for _ in range(n):
        word = set(input()[4:-4]) - basic_alpha
        if len(word) <= k:
            words.append(word)
            alpha_count += Counter(word)
            alpha = alpha | word
    
    if k <= 0:
        return 0

    max_cnt = 0
    for combi in combinations(alpha, k):
        cnt = 0
        for word in words:
            if len(word - set(combi)) == 0:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt

print(solution())