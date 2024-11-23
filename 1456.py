class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        max_vol = 0
        current_vol = 0
        for i in range(k):
            if s[i] in vowels:
                current_vol += 1

        max_vol = current_vol

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                current_vol -= 1
            if s[i] in vowels:
                current_vol += 1
            
            max_vol = max(max_vol, current_vol)
        return max_vol