# Definition for singly-linked list.

from typing import Optional
from util.data_structures import ListNode
from util.tests import run_test_case_linked_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        front = ListNode()
        current = front
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10
        if carry:
            current.next = ListNode(carry)
        return front.next
   

if __name__ == "__main__":
    s = Solution()
    run_test_case_linked_list(s.addTwoNumbers, ([2, 4, 3], [5, 6, 4]), [7, 0, 8])
    run_test_case_linked_list(s.addTwoNumbers, ([0], [0]), [0])
    run_test_case_linked_list(s.addTwoNumbers, ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([0, 1], [0, 1, 2]), [0, 2, 2])
    run_test_case_linked_list(s.addTwoNumbers, ([0, 1, 2], [0, 1]), [0, 2, 2])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1], [1, 1]), [2, 2])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1], [1, 1, 1]), [2, 2, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1, 1], [1, 1]), [2, 2, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1, 1], [1, 1, 1]), [2, 2, 2])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1, 1], [1, 1, 1, 1]), [2, 2, 2, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1, 1, 1], [1, 1, 1]), [2, 2, 2, 1])
    run_test_case_linked_list(s.addTwoNumbers, ([1, 1, 1, 1], [1, 1, 1, 1]), [2, 2, 2, 2])
    run_test_case_linked_list(s.addTwoNumbers, ([], []), [])