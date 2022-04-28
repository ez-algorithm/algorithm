import sys

input = sys.stdin.readline

chars = [input().strip().ljust(15) for _ in range(5)]
print("".join("".join(str) for str in list(zip(*chars))).replace(" ", ""))
