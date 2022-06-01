def solution(places):
    answer = [1 for _ in range(len(places))]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def search(sr, sc):
        visited[sr][sc] = True
        queue = [(sr, sc)]

        while queue:
            vr, vc = queue.pop()
            for d in range(4):
                wr, wc = vr + dr[d], vc + dc[d]
                dist = abs(sr - wr) + abs(sc - wc)

                if -1 < wr < 5 and -1 < wc < 5 and not visited[wr][wc] and dist <= 2:
                    if place[wr][wc] == "P":
                        return False

                    visited[wr][wc] = True
                    if place[wr][wc] != "X":
                        queue.append((wr, wc))
        return True

    for idx, place in enumerate(places):
        visited = [[False for _ in range(5)] for _ in range(5)]
        for r in range(5):
            for c in range(5):
                if not visited[r][c] and place[r][c] == "P":
                    if not search(r, c):
                        answer[idx] = 0
    return answer
