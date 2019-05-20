# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        explored = set([])
        res = []
        stack = [(root, 0)]
        
        if not root:
            return res
        
        while stack:
            node, level = stack.pop()
            if level not in explored:
                explored.add(level)
                res.append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))  
        return res
        