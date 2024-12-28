from util.tests import run_test_case

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    

if __name__ == "__main__":
    s = Solution()
    run_test_case(s.strStr, ["hello", "ll"], 2)
    run_test_case(s.strStr, ["aaaaa", "bba"], -1)
    run_test_case(s.strStr, ["", ""], 0)
    run_test_case(s.strStr, ["a", ""], 0)
    run_test_case(s.strStr, ["", "a"], -1)
    run_test_case(s.strStr, ["mississippi", "issip"], 4)
    run_test_case(s.strStr, ["mississippi", "issipi"], -1)
    run_test_case(s.strStr ,["mississippi", "pi"], 9)
    run_test_case(s.strStr, ["mississippi", "mississippi"], 0)
    run_test_case(s.strStr, ["mississippi", "mississippii"], -1)
    run_test_case(s.strStr, ["mississippi", "mississipp"], 0)
    run_test_case(s.strStr, ["mississippi", "iss"], 1)
