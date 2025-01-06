#!/usr/bin/env python3

from typing import List
from util.tests import run_test_case

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
    

if __name__ == "__main__":
    s = Solution()
    run_test_case(s.searchInsert, ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 5)  
    run_test_case(s.searchInsert, ([], 0), 0)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 5), 2)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 2), 1)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 7), 4)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 0), 0)
    run_test_case(s.searchInsert, ([1], 0), 0)
    run_test_case(s.searchInsert, ([1], 2), 1)
    run_test_case(s.searchInsert, ([1, 3], 2), 1)
    run_test_case(s.searchInsert, ([1, 3], 4), 2)
    run_test_case(s.searchInsert, ([1, 3], 0), 0)
