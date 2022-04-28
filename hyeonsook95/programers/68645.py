def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]

    dr = [1, 0, -1]
    dc = [0, 1, -1]

    r, c, d = 0, 0, 0
    for num in range(1, (n * (n + 1) // 2) + 1):
        maps[r][c] = num
        if not (
            -1 < r + dr[d] < n
            and -1 < c + dc[d] <= r
            and maps[r + dr[d]][c + dc[d]] == 0
        ):
            d = (d + 1) % 3
        r += dr[d]
        c += dc[d]

    maps = [list(filter(lambda x: x != 0, m)) for m in maps]
    return sum(maps, [])
