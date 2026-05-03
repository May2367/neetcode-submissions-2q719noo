# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head

        curr = head.next
        prev = head
        while curr.next != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = None
        head = curr
        head.next = prev

        return head