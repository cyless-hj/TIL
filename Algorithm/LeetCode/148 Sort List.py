# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while head != None:
            arr.append(head.val)
            head = head.next

        arr.sort()

        List = ListNode(0)
        answer = List

        for n in arr:
            List.next = ListNode(n)
            List = List.next
            
        return answer.next