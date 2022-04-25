from collections import defaultdict


def solution(n, words):
    turns = [[] for _ in range(n)]
    dictionary = defaultdict(int)

    prev = words[0][0]
    for idx, word in enumerate(words):
        if prev[-1] != word[0] or dictionary[word]:
            return [(idx % n) + 1, len(turns[idx % n]) + 1]

        turns[idx % n].append(word)
        dictionary[word] += 1
        prev = word

    return [0, 0]
