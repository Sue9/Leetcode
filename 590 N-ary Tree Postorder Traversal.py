# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:48:35 2019

@author: Sue

590. N-ary Tree Postorder Traversal
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorderHelper(self, root, l):
        """
        :type root: Node
        :type l: List[int]
        :rtype: List[int]
        """
        if (root is None):
            return l
        
        for i in root.children:
            l = self.postorderHelper(i, l)
        l.append(root.val)
        return l
        
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        return self.postorderHelper(root, [])