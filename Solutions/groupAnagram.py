
from collections import defaultdict
from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
    
        memory = defaultdict(list)

        for s in strs:
            memory[(''.join(sorted(s)))].append(s)

        return list(memory.values())


if __name__ == '__main__':

    strs = ["eat","tea","tan","ate","nat","bat"]
    Solution().groupAnagrams(strs)