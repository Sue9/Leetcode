# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:02:34 2019

@author: Sue

160. Intersection of Two Linked Lists


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        Algorithm:
            1. get length of two lists, and record the last val to check if its same
            2. pointing to the first place of the shorter list, and the (lengthLong - lengthShort) position of the longer list
            3. find the same val position, or return False
        """
        
        p1 = headA
        p2 = headB
        
        len1 = 0
        len2 = 0
        
        while(p1):
            len1 += 1
            p1 = p1.next
        
        while(p2):
            len2 += 1
            p2 = p2.next
        
        diff = abs(len1 - len2)
        if(len1 > len2):
            long = headA
            short = headB
        else:
            long = headB
            short = headA
        
        while(diff > 0):
            long = long.next
            diff -= 1
            
        while(short != long):
            short = short.next
            long = long.next
        
        return short
        
            
        
        
        