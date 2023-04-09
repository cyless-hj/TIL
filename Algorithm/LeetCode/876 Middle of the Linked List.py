# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        cnt = 0
        while first.next:
            first = first.next
            cnt += 1
        
        half = cnt // 2 + cnt % 2
        while half > 0:
            head = head.next
            half -= 1

        return head