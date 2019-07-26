# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        temp = head
        odd = even = new_head = None
        i = 1
        
        while temp != None:
            if i%2:
                if odd == None:
                    odd = ListNode(temp.val)
                    new_head = odd
                else:
                    odd.next = ListNode(temp.val)
                    odd = odd.next
            
            i += 1
            temp = temp.next
        
        # reset
        i = 2
        temp = head.next
        
        while temp != None:
            if i%2 == 0:
                if even == None:
                        even = ListNode(temp.val)
                        # set up evens
                        odd.next = even
                else:
                    even.next = ListNode(temp.val)
                    even = even.next
            i += 1
            temp = temp.next
