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
        :rtype(subtree tile, sumNode): (int, int)
        """
        if (root is None):
            return (0, 0)
            
        if (root.left is None) and (root.right is None):
            return (0, 0)
            
        elif (root.left is None) and (root.right is not None):
            leftTilt = 0
            leftNodes = 0
            (rightTilt, rightNodes) = self.findTiltHelper(root.right)
            thisTilt = abs(rightNodes + root.right.val)
        
        elif (root.left is not None) and (root.right is None):
            (leftTilt, leftNodes) = self.findTiltHelper(root.left)
            rightTilt = 0
            rightNodes = 0
            thisTilt = abs(leftNodes + root.left.val)
        else: 
            (leftTilt, leftNodes) = self.findTiltHelper(root.left)
            (rightTilt, rightNodes) = self.findTiltHelper(root.right)
            thisTilt = abs(root.left.val + leftNodes - root.right.val - rightNodes)
            
        
        return (leftTilt + rightTilt + thisTilt, leftNodes + rightNodes)
        
        
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (tilt, sumNodes) = self.findTiltHelper(root)
        return tilt
