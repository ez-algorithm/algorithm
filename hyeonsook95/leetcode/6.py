class Solution:
    def convert(self, s, numRows):
        maps = [["" for _ in range(numRows)]]
        if numRows == 1:
            return s

        dr = [0, 1]
        dc = [1, -1]

        d, r, c = -1, 0, 0
        for char in s:
            maps[r][c] = char

            if c == 0 or c == numRows - 1:
                d = (d + 1) % 2
            if d == 1:
                maps.append(["" for _ in range(numRows)])

            r += dr[d]
            c += dc[d]

        answer = ""
        for row in list(zip(*maps)):
            answer += "".join(row)

        return answer
\
