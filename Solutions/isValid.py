
class Solution:

    def isValid(self, s: str) -> bool:

        brackets = []
        left_b = ('(', '[', '{')
        right_b = (')',']','}')

        for char in s:

            if char in left_b:
                brackets.append(char)

            elif not brackets or left_b.index(brackets.pop()) != right_b.index(char):
                return False
        
        return not brackets


if __name__ == '__main__':

    s = "()"
    Solution().isValid(s)

    