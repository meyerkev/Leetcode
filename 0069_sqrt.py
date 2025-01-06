#!/bin/bash python3
from util.tests import run_test_case

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        start = 1
        end = x
        while start < end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid
        return start - 1
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.mySqrt, (4,), 2)
    run_test_case(s.mySqrt, (8,), 2)
    run_test_case(s.mySqrt, (0,), 0)
    run_test_case(s.mySqrt, (1,), 1)
    run_test_case(s.mySqrt, (2,), 1)
    run_test_case(s.mySqrt, (3,), 1)
    run_test_case(s.mySqrt, (5,), 2)
    run_test_case(s.mySqrt, (6,), 2)
    run_test_case(s.mySqrt, (7,), 2)
    run_test_case(s.mySqrt, (9,), 3)
    run_test_case(s.mySqrt, (16,), 4)
    run_test_case(s.mySqrt, (10000,), 100)
    run_test_case(s.mySqrt, (1000000000,), 31622)