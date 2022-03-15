N = int(input())

size = (N - 2) * 2 + 1

border = "*" * N + " " * size + "*" * N
middle = "*" + " " * (N - 2) + "*" + " " * (N - 2) + "*"
inside = "*" + " " * (N - 2) + "*"

dump = 1
blank = -1
for h in range(size + 2):
    blank += dump
    if blank == 0:
        print(border)
    elif h == (size + 2) // 2:
        print(" " * blank + middle)
        dump = -1
    else:
        print((" " * blank) + inside + " " * (size - (blank * 2)) + inside)
