from util.tests import run_test_case
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            while prefix and strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix)-1]

        return prefix
    
if __name__ == "__main__":
    run_test_case(Solution().longestCommonPrefix, (["flower","flow","flight"],), "fl")
    run_test_case(Solution().longestCommonPrefix, (["dog","racecar","car"],), "")
    run_test_case(Solution().longestCommonPrefix, (["dog"],), "dog")
    run_test_case(Solution().longestCommonPrefix, (["dog", "dog", "dog"],), "dog")
    run_test_case(Solution().longestCommonPrefix, (["", "iamaverylongword"],), "")