from typing import Optional
from util.data_structures import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        two = one = head

        while two and two.next:
            one = one.next
            two = two.next.next
            if one == two:
                return True
            
        return False