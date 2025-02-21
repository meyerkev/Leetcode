from typing import Optional
from util.data_structures import TreeNode
from util.tests import run_test_case

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isBalancedHelper(root) != -1
    
    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.isBalancedHelper(root.left)
        right = self.isBalancedHelper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
if __name__ == '__main__':
    s = Solution()
    run_test_case(s.isBalanced, (TreeNode.from_list([3,9,20,None,None,15,7]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,2,3,3,None,None,4,4]),), False)
    run_test_case(s.isBalanced, (TreeNode.from_list([]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,3]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,3,4]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,3,4,5]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,3,4,5,6]),), True)
    run_test_case(s.isBalanced, (TreeNode.from_list([1,2,3,4,5,6,7]),), True)