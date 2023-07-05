# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr_node = root
        if p.val == curr_node.val or q.val == curr_node.val:
            return curr_node

        elif (p.val < curr_node.val and q.val > curr_node.val) or (q.val < curr_node.val and p.val > curr_node.val):
            return curr_node

        elif p.val < curr_node.val and q.val < curr_node.val:
            curr_node = curr_node.left
            
        else:
            curr_node = curr_node.right
            print(curr_node)
        
        return self.lowestCommonAncestor(curr_node, p, q)
