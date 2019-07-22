# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        back = head
        forward = head.next
        
        while forward != None:
            # save the next value before we break the link
            temp = forward.next
            
            # change direction of link and set back poiter to current  pointer
            forward.next = back
            back = forward
            
            # set forward to the next available node
            forward = temp
            
        # loop is done, change direction of head and set new head
        head.next = None
        head = back
        
        return head