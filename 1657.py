from collectins import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        
        return sorted(freq1.values()) == sorted(freq2.values())

        # if len(word1) != len(word2):
        #     return False
        # if set(word1) != set(word2):
        #     return False
        
        # freq1 = {}
        # freq2 = {}

        # word1 = list(word1)
        # word2 = list(word2)
        # word1.sort()
        # word2.sort()

        # for letter in word1:
        #     if letter in freq1:
        #         freq1[letter] += 1
        #     else:
        #         freq1[letter] = 1
        # for letter in word2:
        #     if letter in freq2:
        #         freq2[letter] += 1
        #     else:
        #         freq2[letter] = 1

        # if sorted(freq1.values()) != sorted(freq2.values()):
        #     return False
        # return True