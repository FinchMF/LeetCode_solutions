class Solution:
    def lengtOfLongestSubstring(self, s):
        max_, start, chars = 0, 0, {}
        for idx in range(len(s)):
            if s[idx] in chars and start <= chars[s[idx]]: start = chars[s[idx]] + 1
            else: max_ = max(max_, idx - start + 1)
            chars[s[idx]] = idx
        return max_