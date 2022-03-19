class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "]": "[", "}": "{"}
        temp = []

        for char in s:
            if char in parentheses.values():
                temp.append(char)
            elif char in parentheses.keys():
                if temp and temp[-1] == parentheses[char]:
                    temp.pop()
                else:
                    return False

        if temp:
            return False
        return True
