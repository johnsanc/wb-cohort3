# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        size = 0
        
        temp = head
        
        while temp != None:
            size += 1
            temp = temp.next
        
        rounds = size // k
        
        if rounds == 0 :
            return head
        
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head
        
        for _ in range(rounds):
            before = prev.next 
            after = before.next
            
            for _ in range(0, k-1):
                before.next = after.next
                after.next = prev.next
                prev.next = after
                after = before.next
            
            prev = before
            
        return new_head.next