# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True