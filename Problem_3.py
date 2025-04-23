#Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    # Function to delete a node in the middle of a singly linked list.
    def deleteNode(self, node):
        #code here
        while node.next.next!=None:
            node.data = node.next.data
            node = node.next
        
        node.data = node.next.data
        node.next =None
            