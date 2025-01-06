#!/bin/bash

from util.tests import run_test_case

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.addBinary, ("11", "1"), "100")
    run_test_case(s.addBinary, ("1010", "1011"), "10101")
    run_test_case(s.addBinary, ("0", "0"), "0")
    run_test_case(s.addBinary, ("0", "1"), "1")
    run_test_case(s.addBinary, ("1", "0"), "1")
    run_test_case(s.addBinary, ("1", "1"), "10")
    run_test_case(s.addBinary, ("1", "11"), "100")
    run_test_case(s.addBinary, ("11", "1"), "100")
    run_test_case(s.addBinary, ("11", "11"), "110")
    run_test_case(s.addBinary, ("111", "111"), "1110")
    run_test_case(s.addBinary, ("1111", "1111"), "11110")
    run_test_case(s.addBinary, ("11111", "1"), "100000")
