def solution(n, words):
    visited = [words[0]]

    for i in range(1, len(words)):
        if len(words[i]) > 1:
            if words[i-1][-1] != words[i][0] or words[i] in visited:
                return [(i%n)+1, (i//n)+1]
            else:
                visited.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]
    return [0,0]