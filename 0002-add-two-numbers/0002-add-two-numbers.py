# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop through lists l1 and l2 until both are empty AND there is no carry left
        while l1 or l2 or carry:
            # Get values from current nodes, default to 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            out_val = total % 10
            
            # Create a new node with the single-digit result
            current.next = ListNode(out_val)
            current = current.next
            
            # Move to the next nodes in the lists if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next
        