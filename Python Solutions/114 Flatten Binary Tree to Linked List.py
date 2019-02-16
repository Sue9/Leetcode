# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:48:42 2019

@author: Sue

114. Flatten Binary Tree to Linked List
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        
        """
        Algorithm:
        1. move right child to left child right-most leaf
        2. flatten left child
        3. move left child to the right
        """
        
        if (root is None) or (root.left is None):
            return root
        
        rootRightChild = self.flatten(root.right)
        tp = root.left
        
        #find right-most leaf
        print("before while tp val = ", tp.val)
        while (tp.right != None):
            tp = tp.right
            print("in while, tp val = ", tp.val)
        
        tp.right = rootRightChild
        
        root.right = self.flatten(root.left)
        root.left = None
        
        
        
        
        