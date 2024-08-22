from typing import List

from util import run_test_case

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [x for x in enumerate(nums)]

        nums = sorted(nums, key=lambda x: x[1])
        start = 0
        end = len(nums) - 1
        while start < end:
            result = nums[start][1] + nums[end][1]
            if result < target:
                start += 1
            elif result > target:
                end -= 1
            else:
                # Congratulations! We found the answer
                # But now we must sort it
                if nums[start][0] < nums[end][0]:
                    return [nums[start][0], nums[end][0]]
                else:
                    return [nums[end][0], nums[start][0]]       
                     
        raise ValueError("No two sum solution")
    
if __name__ == "__main__":
    s = Solution()
    run_test_case(s.twoSum, ([2, 7, 11, 15], 9), [0, 1])
    run_test_case(s.twoSum, ([3, 2, 4], 6), [1, 2])
    run_test_case(s.twoSum, ([3, 3], 6), [0, 1])
    run_test_case(s.twoSum, ([3, 2, 3], 6), [0, 2])
    run_test_case(s.twoSum, ([3, 2, 4], 5), [0, 1])
    run_test_case(s.twoSum, ([3, 2, 4], 6), [1, 2])
    run_test_case(s.twoSum, ([3, 2, 4], 7), [0, 2])
    run_test_case(s.twoSum, ([7, 6, 5], 13), [0, 1])
    run_test_case(s.twoSum, ([7, 6, 5], 12), [0, 2])
    run_test_case(s.twoSum, ([7, 6, 5], 11), [1, 2])



