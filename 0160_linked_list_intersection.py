from typing import Optional
from util.data_structures import ListNode

class Solution:
    # Two answers
    # 1. Drop A into a set of ListNodes, then iterate through B and check if the node is in the set
    # 2. Make A and B the same length, then iterate through both and check if the nodes are the same
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        nodeSet = set()
        while headA is not None:
            nodeSet.add(headA)
            headA = headA.next
        
        while headB:
            if headB in nodeSet:
                return headB
            headB = headB.next
        
        return None
    
    def getIntersectionNodeTwo(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        
        while currA:
            lenA += 1
            currA = currA.next
        
        while currB:
            lenB += 1
            currB = currB.next
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
