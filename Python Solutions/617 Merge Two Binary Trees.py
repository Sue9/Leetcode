# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:00:39 2018

@author: zhaoxu

617 Merge Two Binary Trees
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 != None and t2 == None:
            return t1
        
        if t1 == None and t2 != None:
            return t2
        
        if t1 == None and t2 == None:
            return None
        
        mt = TreeNode(t1.val + t2.val)
        mt.left = self.mergeTrees(t1.left, t2.left)
        mt.right= self.mergeTrees(t1.right,t2.right)
        
        return mt
        
        
            
            
        