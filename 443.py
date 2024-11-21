from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            curr = chars[read]
            length = 1

            while read + 1 < len(chars) and chars[read + 1] == curr:
                length += 1
                read += 1
            chars[write] = curr
            write += 1

            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1

            read += 1
        return write        

