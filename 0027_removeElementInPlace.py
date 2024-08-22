from typing import List, Tuple
from util.tests import run_test_case_custom_test, CustomTestCase

class Solution (CustomTestCase):
    def test(self, input: Tuple[List[int], int], expected: Tuple[int, List[int]]):
        result = self.removeElement(*input)
        assert result == expected[0], f"Expected {expected[0]} numbers, but got {result}"
        for i in range(expected[0]):
            assert input[0][i] == expected[1][i], f"Expected {expected[1][i]} at index {i}, but got {input[0][i]}"
        

    def removeElement(self, nums: List[int], val: int) -> int:
        print(f"Input: {nums}, {val}")
        # Initialize a pointer to the first element
        i = 0
        # Iterate through the list
        for j in range(len(nums)):
            # If the element at the current index is different from the value to be removed
            if nums[j] != val:
                # Set the element at the pointer to the element at the current index
                nums[i] = nums[j]
                # Increment the pointer
                i += 1
        # Return the length of the list up to the pointer
        return i
    
if __name__ == "__main__":
    s = Solution()
    run_test_case_custom_test(s, [[3,2,2,3], 3], (2, [2,2]))
    run_test_case_custom_test(s, [[0,1,2,2,3,0,4,2], 2], (5, [0,1,3,0,4]))
    run_test_case_custom_test(s, [[1], 1], (0, []))
    run_test_case_custom_test(s, [[1,1], 1], (0, []))
    run_test_case_custom_test(s, [[1,2], 1], (1, [2]))
    run_test_case_custom_test(s, [[1,2,3], 1], (2, [2,3]))
    run_test_case_custom_test(s, [[1,1,1], 1], (0, []))
    run_test_case_custom_test(s, [[1,1,1], 2], (3, [1,1,1]))
    run_test_case_custom_test(s, [[3, 3, 3], 3], (0, []))
    run_test_case_custom_test(s, [[], 3], (0, []))