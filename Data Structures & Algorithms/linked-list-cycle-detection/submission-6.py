# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Fast and Slow Pointer

        slow = head
        fast = head.next if head != None else None

        while fast:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next if fast.next != None else None

        return False