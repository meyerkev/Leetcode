from typing import Optional
from util.data_structures import ListNode
from util.tests import run_test_case_linked_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to point to the head of the merged list
        dummy = ListNode()
        # Create a pointer to the dummy node
        current = dummy
        # While both lists have elements
        while list1 and list2:
            # If the value of list1 is less than the value of list2
            if list1.val < list2.val:
                # Point the next node of the current node to list1
                current.next = list1
                # Move list1 to the next node
                list1 = list1.next
            else:
                # Point the next node of the current node to list2
                current.next = list2
                # Move list2 to the next node
                list2 = list2.next
            # Move the current node to the next node
            current = current.next
        # If list1 has elements left
        if list1:
            # Point the next node of the current node to list1
            current.next = list1
        # If list2 has elements left
        if list2:
            # Point the next node of the current node to list2
            current.next = list2
        # Return the next node of the dummy node
        return dummy.next
        
if __name__ == "__main__":
    s = Solution()
    run_test_case_linked_list(s.mergeTwoLists, ([1,2,4], [1,3,4]), [1,1,2,3,4,4])
    run_test_case_linked_list(s.mergeTwoLists, ([], []), [])
    run_test_case_linked_list(s.mergeTwoLists, ([], [0]), [0])
    run_test_case_linked_list(s.mergeTwoLists, ([0], []), [0])
    run_test_case_linked_list(s.mergeTwoLists, ([1,2,3], []), [1,2,3])
    run_test_case_linked_list(s.mergeTwoLists, ([], [1,2,3]), [1,2,3])
    run_test_case_linked_list(s.mergeTwoLists, ([1,2,3], [4,5,6]), [1,2,3,4,5,6])