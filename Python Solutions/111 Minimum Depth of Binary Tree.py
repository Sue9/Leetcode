# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:35:43 2019

@author: Sue

111. Minimum Depth of Binary Tree

"""

class Solution(object):
    
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if(root is None):
            return 0
        
        if(root.left is None) and (root.right is None):
            return 1
        
        elif(root.left is None) and (root.right is not None):
            return 1 + self.minDepth(root.right)
        
        elif(root.left is not None) and (root.right is None):
            return 1 + self.minDepth(root.left)
        else:        
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1