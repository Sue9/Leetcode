# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:02:48 2019

@author: Sue

872. Leaf-Similar Trees
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        

class Solution(object):
    def leafSequence(self, root):
        """
        :type root: TreeNode
        :rtype: List[Int]
        """
        if (root is None):
            return []
        
        if (root.left is None) and (root.right is None):
            return [root.val]
        
        l1 = self.leafSequence(root.left)
        l2 = self.leafSequence(root.right)
        
        return l1+l2
        
        
        
        
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafSequence(root1) == self.leafSequence(root2)