# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:57:28 2019

@author: Sue

876. Middle of the Linked List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        l = []
        
        while p:
            l.append(p.val)
            p = p.next
        
        m = int(len(l) / 2) + 1
               
        while m:
            head = head.next
            m -= 1
            
        return head