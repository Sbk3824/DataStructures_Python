# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return root
        
        dMap = {}
        level = [(root, 0)]
        
        while level:
            newLevel = []
            for node, distance in level:
                if distance not in dMap:
                    dMap[distance] = []
                dMap[distance].append(node.val)
                
                if node.left:
                    newLevel.append((node.left, distance - 1))
                if node.right:
                    newLevel.append((node.right, distance + 1))
            level = newLevel
        
        res = [0] * len(dMap)
        offset = -min(dMap.keys())
        print(offset)
        for k, l in dMap.items():
            res[k + offset] = l
        return res