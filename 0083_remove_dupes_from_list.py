#!/usr/bin/env python3

from util.tests import run_test_case_linked_list
from util.data_structures import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pre = head
        tail = head.next

        while tail:
            if pre.val == tail.val:
                pre.next = tail.next
            else:
                pre = tail
            tail = tail.next
        return head

if __name__ == "__main__":
    s = Solution()
    run_test_case_linked_list(s.deleteDuplicates, ([1, 1, 2],),  [1, 2])
    run_test_case_linked_list(s.deleteDuplicates, ([1, 1, 2, 3, 3],), [1, 2, 3])
    run_test_case_linked_list(s.deleteDuplicates, ([1, 1, 1],), [1])
    run_test_case_linked_list(s.deleteDuplicates, ([1, 1, 1, 2, 2, 3],), [1, 2, 3])
    run_test_case_linked_list(s.deleteDuplicates, ([1, 2, 3],), [1, 2, 3])
    run_test_case_linked_list(s.deleteDuplicates, (None,), None)