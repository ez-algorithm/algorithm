def solution(numbers, target):
    def dfs(idx, sum, case):
        if idx == len(numbers):
            if target == sum:
                return case + 1
            return case

        for t in [1, -1]:
            case = dfs(idx + 1, (sum + numbers[idx] * t), case)
        return case

    return dfs(0, 0, 0)
