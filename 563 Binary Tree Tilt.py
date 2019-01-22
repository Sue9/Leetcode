# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:31:34 2019

@author: Sue

563 Binary Tree Tilt
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def findTiltHelper(self, root):
        """
        :type root: TreeNode
        :rtype(subtree tilt): int
        """
        if (root is None):
            return 0
            
        if (root.left is None) and (root.right is None):
            return 0
        
        leftTilt = self.findTiltHelper(root.left)
        rightTilt = self.findTiltHelper(root.right)
        thisTilt = abs(self.sumNodes(root.left) - self.sumNodes(root.right))
        
        return (leftTilt + rightTilt + thisTilt)
        
    
    def sumNodes(self, root):
        """
        Return all node values of this tree
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0
        
        return self.sumNodes(root.left) + self.sumNodes(root.right) + root.val
    
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt = self.findTiltHelper(root)
        return tilt
