# Time Complexity = O(m+n)
# Space Complexity = O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        up = headA
        down = headB

        upflag = False
        downflag = False
        while up!=None and down!=None:
            if up==down:
                return up
            up=up.next
            down=down.next

            if up==None and not downflag:
                up=headB
                downflag = True
            if down == None and not upflag:
                down = headA
                upflag = True
            
        return None
            


        