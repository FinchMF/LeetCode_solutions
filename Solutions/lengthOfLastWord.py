from typing import List

class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        length_of_w = 0

        s = s[::-1]

        idx = -1

        for char in s: 

            idx += 1
            if char != ' ':

                break

        if idx == -1: return 0

        else:

            for i in range(idx, len(s)):

                if s[i] != ' ': length_of_w += 1

                else:

                    break

            return length_of_w


if __name__ == '__main__':

    s = 'Hello World'

    print(Solution().lengthOfLastWord(s))

                

