from itertools import product


def solution(numbers, target):
    cnt = 0
    n = len(numbers)
    numbers = [[-number, number] for number in numbers]
    for num in product(*numbers):
        if sum(num) == target:
            cnt += 1
    return cnt
