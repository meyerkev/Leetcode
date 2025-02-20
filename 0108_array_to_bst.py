from typing import List, Optional
from util.data_structures import TreeNode
from util.tests import CustomTestCase, run_test_case_custom_test

class Solution(CustomTestCase):
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Split array in half, make the middle element the root, and recursively
        # build the left and right subtrees

        if not nums:
            return None
        
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)
    
    def sortedArrayToBSTHelper(self, nums: List[int], front, end) -> Optional[TreeNode]:
        if front > end:
            return None
        mid = (front + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, front, mid - 1)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, end)
        return root
    
    def test(self, input, expected_output):
        nums = input
        result = self.sortedArrayToBST(nums)
        print(f"Result: {result}")
        if result is None:
            assert expected_output is None
            return
        test_output = TreeNode.from_list(expected_output)
        # I'm only willing to do so much work to compare contents of two trees
        assert result.count_nodes() == test_output.count_nodes()
        assert result.height() == test_output.height()



if __name__ == "__main__":
    s = Solution()
    run_test_case_custom_test(s, ([-10,-3,0,5,9]), [-10, -3, 0, 5, 9])
    run_test_case_custom_test(s, ([1,3]), [1, 3])
    run_test_case_custom_test(s, ([1]), [1])
    run_test_case_custom_test(s, ([1,2,3,4,5,6,7]), [4, 2, 6, 1, 3, 5, 7])
    run_test_case_custom_test(s, ([1,2,3,4,5,6,7,8]), [5, 3, 7, 2, 4, 6, 8, 1])
    run_test_case_custom_test(s, ([]), None)
        # Expected: [-10, -3, 0, 5, 9]
        # Explanation: The resulting tree is:
        #       0
        #      / \
        #    -3   9
        #    /   /
        # -10  5

