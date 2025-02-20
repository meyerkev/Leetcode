from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst: List):
        if not lst:
            return None
        head = cls(lst[0])
        current = head
        for i in range(1, len(lst)):
            current.next = cls(lst[i])
            current = current.next
        return head

def convert_list_to_linked_list(lst):
    return ListNode.from_list(lst)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, lst: List):
        if not lst:
            return None
        head = cls(lst[0])
        queue = [head]
        index = 0
        child = 1
        while index < len(queue):
            current = queue[index]
            if child < len(lst) and lst[child] is not None:
                current.left = cls(lst[child])
                queue.append(current.left)
            child += 1
            if child < len(lst) and lst[child] is not None:
                current.right = cls(lst[child])
                queue.append(current.right)
            child += 1
            index += 1
        
        return head
    
    def __repr__(self):
        return f"TreeNode({self.val}, {self.left.val if self.left else None}, {self.right.val if self.right else None})"

    def print_tree_by_layer(self):
        queue = [(0, self)]
        current_layer = 0
        print("Layer", current_layer)
        while queue:
            layer, current = queue.pop(0)
            if layer != current_layer:
                print()
                print("Layer", layer)
                current_layer = layer
            print(current)
            if current.left:
                queue.append((layer + 1, current.left))
            if current.right:
                queue.append((layer + 1, current.right))
        print()

    def height(self):
        if not self:
            return 0
        return 1 + max(self.left.height() if self.left else 0, self.right.height() if self.right else 0)
    
    def count_nodes(self):
        if not self:
            return 0
        return 1 + (self.left.count_nodes() if self.left else 0) + (self.right.count_nodes() if self.right else 0)

    # equals method for testing
    def __eq__(self, other):
        # left and right can either be None or a TreeNode
        if not other:
            return False
        if self.val != other.val:
            return False
        if not (self.left is None and other.left is None) and not self.left == other.left:
            return False
        if not (self.right is None and other.right is None) and not self.right == other.right:
            return False
        return True