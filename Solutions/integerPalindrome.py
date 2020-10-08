class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if integer palindrome is true
        return str(x) == str(x)[::-1]
