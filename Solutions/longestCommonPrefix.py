
class Solution:
    def longestCommonPrefix(self, s):
        jdx = 0
        while s and all(jdx < len(s[idx]) and jdx < len(s[idx - 1]) 
                                          and s[idx][jdx] == s[idx - 1][jdx] for idx in range(len(s))):

            jdx += 1
        
        return s[0][:jdx] if jdx else ''
