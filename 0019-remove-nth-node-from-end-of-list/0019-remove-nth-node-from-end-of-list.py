class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to handle edge cases easily 
        # (e.g., removing the very first node of the list)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Advance 'fast' pointer by n + 1 steps so that the gap 
        # between 'slow' and 'fast' is exactly n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until 'fast' reaches the end of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # 'slow' is now positioned right before the node to be removed
        slow.next = slow.next.next

        return dummy.next