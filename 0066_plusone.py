
#!/bin/bash
from typing import List
from util.tests import run_test_case


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.plusOne, ([1, 2, 3],), [1, 2, 4])
    run_test_case(s.plusOne, ([4, 3, 2, 1],), [4, 3, 2, 2])
    run_test_case(s.plusOne, ([9, 9, 9],), [1, 0, 0, 0])
    run_test_case(s.plusOne, ([0],), [1])
    run_test_case(s.plusOne, ([9],), [1, 0])
    run_test_case(s.plusOne, ([1, 9],), [2, 0])