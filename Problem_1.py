#Time Complexity = O(1)
# Space Complexity = O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.dfs(root)
        

    def next(self) -> int:
        if self.hasNext():
            node = self.stack.pop()
            self.dfs(node.right)
            return node.val
        else:
            return None
        

    def hasNext(self) -> bool:
        return len(self.stack)>=1


    def dfs(self,node):
        while node!=None:
            self.stack.append(node)
            node = node.left
            


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()