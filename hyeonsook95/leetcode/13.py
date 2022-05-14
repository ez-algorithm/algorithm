class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0
        pre_number = roman_to_int[s[0]]

        for cur_number in s[1:]:
            # 이전의 값보다 현재의 값이 크면 뺄셈 연산으로 변환
            if pre_number < roman_to_int[cur_number]:
                pre_number *= -1

            answer += pre_number
            pre_number = roman_to_int[cur_number]

        answer += pre_number
        return answer
