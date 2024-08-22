from util.tests import run_test_case
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix += c
        return prefix
    
if __name__ == "__main__":
    run_test_case(Solution().longestCommonPrefix, (["flower","flow","flight"],), "fl")
    run_test_case(Solution().longestCommonPrefix, (["dog","racecar","car"],), "")
    run_test_case(Solution().longestCommonPrefix, (["dog"],), "dog")
    run_test_case(Solution().longestCommonPrefix, (["dog", "dog", "dog"],), "dog")
    run_test_case(Solution().longestCommonPrefix, (["", "iamaverylongword"],), "")