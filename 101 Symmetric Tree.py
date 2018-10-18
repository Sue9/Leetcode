# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:05:42 2018

@author: zhaoxu

101 Symmetric Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    
    def symmetricTree(self, root):
        if root is None:
            return root
        
        t = TreeNode(root.val)
        t.left = self.symmetricTree(root.right)
        t.right = self.symmetricTree(root.left)
        
        return t
        
    
    def identifyTree(self, leftT, rightT):
        if (leftT is None) and (rightT is None):
            return True
        elif (leftT is None) and (rightT is not None):
            return False
        elif (leftT is not None) and (rightT is None):
            return False
        else:
            return (leftT.val == rightT.val) and self.identifyTree(leftT.left, rightT.left) and self.identifyTree(leftT.right, rightT.right)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
#        recursively
        if root is None:
            return True
        
        return self.identifyTree(self.symmetricTree(root.left) , root.right)
        
        #The way I didn't make out
#        if (root.left is None) and (root.right is None):
#            return True
#        elif (root.left is None) and (root.right is not None):
#            return False
#        elif (root.left is not None) and (root.right is None):
#            return False
#        else:
#            if (root.left.val != root.right.val):
#                return False
#            else:
#                return (root.left.left.val == root.right.right.val) and (root.left.right.val == root.right.left.val) and self.isSymmetric(root.left) and self.isSymmetric(root.right)
#        
        