class Solution:
    def reverse(self, x: int) -> int:
        number = x
        if number >= 0:
            number = str(number)
            number = number[::-1]
            number = int(number)
        
        if number < 0:
            number = abs(number)
            number = str(number)
            number = number[::-1]
            number = int(number)
            number = -number
        if number < -2**31 or number > 2**31 - 1:
            return 0
        return number
        