from typing import List
from util.tests import run_test_case

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 5), 2)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 2), 1)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 7), 4)
    run_test_case(s.searchInsert, ([1, 3, 5, 6], 0), 0)
    run_test_case(s.searchInsert, ([1], 0), 0)
    run_test_case(s.searchInsert, ([1], 1), 0)
    run_test_case(s.searchInsert, ([1], 2), 1)
    run_test_case(s.searchInsert, ([], 103000000), 0)
    run_test_case(s.searchInsert, ([], -103000000), 0)
                  
