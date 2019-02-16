# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:14:07 2019

@author: Sue

589. N-ary Tree Preorder Traversal
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    
    def preorderHelper(self, root, l):
        """
        :type root: Node
        :type l: List[int]
        :rtype: List[int]
        """
        
        l.append(root.val)
        
        if (root.children == []):
            return l
        
        for t in root.children:
            l = self.preorderHelper(t, l)
        
        return l
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if(root is None):
            return []
        return self.preorderHelper(root, [])