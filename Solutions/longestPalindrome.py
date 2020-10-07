class Solution:
    def longestPalindrome(self, s: str) -> str:
        # helper function to parse substrings
        def check(l,r):
            # check from center, moving outwards to find palindrome substring
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            # return substring
            return s[l+1:r]

        
        # counter for print statements
        x = 0
        
        result = ''

        for idx in range(len(s)):
            # use check function to find the longest palindrome substring
            # check both idx and idx + 1 and set result to longest substring
            check_string = check(idx, idx)
            print(f'Test Condition 1: {x} -- {check_string}')
            if check_string > len(result): result = check_string
            check_string = check(idx, idx + 1)
            print(f'Test Condition 2: {x} -- {check_string}')
            if check_string > len(result): result = check_string
            x += 1

        return result