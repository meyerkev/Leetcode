from util.tests import run_test_case

class Solution:
    def isPalindromeSimple(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        if x % 10 == 0: return False
        
        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # Could be off by one
        return x == reversed_x or x == reversed_x // 10
    

if __name__ == "__main__":
    s = Solution()
    run_test_case(s.isPalindrome, (121,), True)
    run_test_case(s.isPalindrome, (-121,), False)
    run_test_case(s.isPalindrome, (10,), False)
    run_test_case(s.isPalindrome, (-101,), False)
    run_test_case(s.isPalindrome, (0,), True)
    run_test_case(s.isPalindrome, (1,), True)
    run_test_case(s.isPalindrome, (11,), True)
    run_test_case(s.isPalindrome, (111,), True)
    run_test_case(s.isPalindrome, (1111,), True)
    run_test_case(s.isPalindrome, (11111,), True)
    run_test_case(s.isPalindrome, (111111,), True)
    run_test_case(s.isPalindrome, (9876543210123456789,), True)
    run_test_case(s.isPalindrome, (98765432101234567890,), False)
    run_test_case(s.isPalindrome, (543454345, ), True)