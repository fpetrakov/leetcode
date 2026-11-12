BRACKETS = {
    "[": "]",
    "(": ")",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in BRACKETS:
                stack.append(BRACKETS[bracket])
                continue
            if len(stack) == 0:
                return False
            closing_bracket = stack.pop()
            if closing_bracket != bracket:
                return False

        return len(stack) == 0
