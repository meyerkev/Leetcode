from typing import List, Tuple
from util.tests import run_test_case_custom_test

class Solution:
    def test(self, input: List[int], expected: Tuple[int, List[int]]):
        result = self.removeDuplicates(input)
        assert result == expected[0], f"Expected {expected[0]} numbers, but got {result}"
        for i in range(expected[0]):
            assert input[i] == expected[1][i], f"Expected {expected[1][i]} at index {i}, but got {input[i]}"
        

    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty, return 0
        if not nums:
            return 0
        # Initialize a pointer to the first element
        i = 0
        # Iterate through the list
        for j in range(1, len(nums)):
            # If the element at the current index is different from the element at the previous index
            if nums[j] != nums[i]:
                # Increment the pointer
                i += 1
                # Set the element at the pointer to the element at the current index
                nums[i] = nums[j]
        # Return the length of the list up to the pointer
        return i + 1
    
if __name__ == "__main__":
    s = Solution()
    run_test_case_custom_test(s, [1,1,2], (2, [1,2]))
    run_test_case_custom_test(s, [0,0,1,1,1,2,2,3,3,4], (5, [0,1,2,3,4]))
    run_test_case_custom_test(s, [], (0, []))
    run_test_case_custom_test(s, [1], (1, [1]))
    run_test_case_custom_test(s, [1,1], (1, [1]))
    run_test_case_custom_test(s, [1,2], (2, [1,2]))
    run_test_case_custom_test(s, [1,2,3], (3, [1,2,3]))
    run_test_case_custom_test(s, [1,1,1], (1, [1]))
