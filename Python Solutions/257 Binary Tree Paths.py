# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:46:03 2019

@author: Sue

257. Binary Tree Paths
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathHelper(self, root, s, res):
        """
        :type root: TreeNode
        :rtype: List[str]
        
        """
        
        if (root is None):
            return
        
        # goes to the leaf node
        if (root.left is None) and (root.right is None):
            s += str(root.val)
            res.append(s)
            s = s[:-1]
            return
        
        #not leaf
        s = s + str(root.val) + "->"
        if (root.left):
            self.pathHelper(root.left, s, res)
        
        if (root.right):
            self.pathHelper(root.right, s, res)
            
        return
        
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if (root is None):
            return []
        
        res = []
        s = ""
        
        self.pathHelper(root, s, res)
        
        return res
        
        