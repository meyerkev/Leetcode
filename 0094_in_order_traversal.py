#!/usr/bin/env python3

from util.tests import CustomTestCase, run_test_case_custom_test
from util.data_structures import TreeNode
from typing import List, Optional

class Solution(CustomTestCase):
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root or root.val is NotImplemented:
            return []

        left_list = self.inorderTraversal(root.left)
        left_list.append(root.val)
        right_list = self.inorderTraversal(root.right)
        left_list.extend(right_list)
        return left_list

    def test(self, input, expected_output):
        t: TreeNode = TreeNode.from_list(input[0])
        # t.print_tree_by_layer() if t else print("Empty tree")
        result = self.inorderTraversal(t)
        assert(result == expected_output)


if __name__ == "__main__":
    s = Solution()
    run_test_case_custom_test(s, ([1, None, 2, 3],), [1, 3, 2])
    run_test_case_custom_test(s, ([1, 2, 3, 4, 5, 6, 7],), [4, 2, 5, 1, 6, 3, 7])    # run_test_case_custom_test(s, ([1,2,3,4,5,None,8,None,None,6,7,9],), [4, 2, 6, 5, 7, 1, 3, 9, 8])
    run_test_case_custom_test(s, ([],), [])
    run_test_case_custom_test(s, ([1],), [1])
    run_test_case_custom_test(s, ([1, None, 0, 3],), [1, 3, 0])

