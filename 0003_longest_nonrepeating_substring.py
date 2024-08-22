from util.tests import run_test_case

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxLen = 0
        for i in range(len(s)):
            setOfChars = set()
            for j in range(i, len(s)):
                if s[j] in setOfChars:
                    maxLen = max(maxLen, j - i)
                    break
                elif j == len(s) - 1:
                    maxLen = max(maxLen, j - i + 1)
                    break
                setOfChars.add(s[j])

        return maxLen
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.lengthOfLongestSubstring, ("abcabcbb",), 3)
    run_test_case(s.lengthOfLongestSubstring, ("bbbbb",), 1)
    run_test_case(s.lengthOfLongestSubstring, ("pwwkew",), 3)
    run_test_case(s.lengthOfLongestSubstring, ("",), 0)
    run_test_case(s.lengthOfLongestSubstring, ("z",), 1)
    run_test_case(s.lengthOfLongestSubstring, ("zz",), 1)
    run_test_case(s.lengthOfLongestSubstring, ("abc",), 3)
    run_test_case(s.lengthOfLongestSubstring, ("ab",), 2)
    run_test_case(s.lengthOfLongestSubstring, ("this is a full sentence with spaces",), 10)
