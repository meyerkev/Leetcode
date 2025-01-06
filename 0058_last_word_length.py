#! /usr/bin/python3
from util.tests import run_test_case

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        return len(s.rsplit(maxsplit=1)[-1])
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.lengthOfLastWord, ("Hello World",), 5)
    run_test_case(s.lengthOfLastWord, ("Hello",), 5)
    run_test_case(s.lengthOfLastWord, ("",), 0)
    run_test_case(s.lengthOfLastWord, ("a ",), 1)
    run_test_case(s.lengthOfLastWord, ("a",), 1)
    run_test_case(s.lengthOfLastWord, (" a",), 1)
    run_test_case(s.lengthOfLastWord, (" a ",), 1)