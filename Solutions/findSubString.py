
import collections

class Solution:

    def findSubString(self, s:str, words: list(str)) -> list(int):

        if not s or not words: return []

        count = collections.Counter(words)
        len_words = len(words[0]) * len(words)
        len_word = len(words)
        count_words = len(words[0])
        result = []

        for idx in range(len(s)  - len_words + 1):

            cur, j = dict(count), idx

            for _ in range(count_words):

                w = s[j:j + len_word]

                if w in cur:

                    if cur[w] == 1: cur.pop(w)
                    else: cur[w] -= 1

                else: break 

                j += len_word

            if not cur: result += idx,
        
        return result


if __name__ == '__main__':

    s, words = "barfoothefoobarman", ["foo","bar"]
    Solution().findSubString(s, words)

    