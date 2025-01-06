#!/bin/bash
from util.tests import CustomTestCase, run_test_case_custom_test
from typing import List

class Solution(CustomTestCase):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
    def test(self, input, expected_output):
        nums1, m, nums2, n = input
        if len(nums1) < m + n:
            nums1 += [None] * (m + n - len(nums1))
        self.merge(nums1, m, nums2, n)
        print(f"Result: {nums1}")
        assert nums1 == expected_output

if __name__ == "__main__":
    s = Solution()
    run_test_case_custom_test(s, ([1,2,3,None, None, None], 3, [2,5,6], 3), [1,2,2,3,5,6])
    run_test_case_custom_test(s, ([1], 1, [], 0), [1])
    run_test_case_custom_test(s, ([], 0, [1], 1), [1])
    run_test_case_custom_test(s, ([0], 0, [1], 1), [1])
    run_test_case_custom_test(s, ([1,2,3,None, None, None], 3, [4,5,6], 3), [1,2,3,4,5,6])
    run_test_case_custom_test(s, ([-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1, None], 12, [0], 1), [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1, 0])
    run_test_case_custom_test(s, ([0, None], 1, [1], 1), [0, 1])
    run_test_case_custom_test(s, ([1, None], 1, [0], 1), [0, 1])