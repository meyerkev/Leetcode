from typing import List, Optional
from util.data_structures import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        result = []
        while queue:
            node = queue.pop()
            if node:
                result.append(node.val)
                queue.append(node.right)
                queue.append(node.left)

        return result