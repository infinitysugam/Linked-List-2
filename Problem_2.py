# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head

        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        

        fast = self.reverse(slow.next)
        slow.next = None
        slow = head

        while fast!=None and slow!=None:
            temp = slow.next
            slow.next = fast

            temp1 = fast.next
            fast.next = temp

            slow =temp
            fast = temp1
    
    def reverse(self,head):
        prev = None
        curr = head

        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev




        

        