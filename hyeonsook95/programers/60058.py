def solution(p):
    # 올바른 괄호 문자열인지 확인
    def is_correct(str):
        stack = []

        for char in str:
            if char == "(":
                stack.append(char)
            elif not stack:
                return False
            else:
                stack.pop()

        if stack:
            return False
        return True

    # 최소 길이의 균형잡힌 문자열과 나머지 문자열로 분리
    def split_uv(w):
        cnt_r, cnt_l = 0, 0
        for idx, char in enumerate(w):
            if char == "(":
                cnt_l += 1
            else:
                cnt_r += 1

            if cnt_r == cnt_l:
                return w[: idx + 1], w[idx + 1 :]

    def convert(w):
        # 입력이 빈 문자열일 경우, 빈 문자열을 반환
        if not w:
            return w

        # 문자열을 u, v로 분리
        u, v = split_uv(w)
        v = convert(v)

        # u가 올바른 문자열이면 v와 반환
        if is_correct(u):
            return u + v

        # 올바른 문자열이 아니면, 반대 괄호를 붙여서 반환
        v = "(" + v + ")"
        for char in u[1:-1]:
            if char == "(":
                v += ")"
            else:
                v += "("
        return v

    return convert(p)
