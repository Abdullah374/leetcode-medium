class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter != '*':
                stack.append(letter)
            else:
                stack.pop()
        stack = ''.join(stack)
        return stack