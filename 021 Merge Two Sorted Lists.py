# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:30:25 2018

@author: Sue


021 Merge Two Sorted Lists 
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
        
        """
        #quite lengthy
        
        if l1 is None and l2 is None:
            return None
        
        if l1 is None and l2 is not None:
            return l2
        
        if l2 is None and l1 is not None:
            return l1
        
        
        if l1.val <= l2.val:
            res = ListNode(l1.val)
            res.next = self.mergeTwoLists(l1.next, l2)
        else:
            res = ListNode(l2.val)
            res.next = self.mergeTwoLists(l1, l2.next)
            
        return res
        
        """