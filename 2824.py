class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            if j == len(str2):
                return True
           
            this = ord(str1[i])
            that = chr((this + 1 - 97)%26 + 97)
            
            if str1[i] == str2[j] or that== str2[j]:
                j += 1
        return j == len(str2)
             

        