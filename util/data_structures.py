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