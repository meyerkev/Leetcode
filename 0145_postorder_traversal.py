from typing import List, Optional
from util.data_structures import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        postorder = []
        while stack:
            node = stack.pop()
            if node:
                postorder.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return postorder[::-1]