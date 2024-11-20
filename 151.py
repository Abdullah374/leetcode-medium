class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        result = ''
        
        s = s.split()
        s = s[::-1]

        for word in s:
            result += f"{word} "

        return result.strip()