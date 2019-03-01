# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:21:46 2019

@author: Sue

019. Remove Nth Node From End of List
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head is None):
            return head
        if(n <= 0):
            return head
        
        size = 0
        cur = head
        while(cur):
            size += 1
            cur = cur.next
        
        if(n > size):
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = head
        
        step = size - n
        while(step >= 1):
            prev = prev.next
            cur = cur.next
            step -= 1
        prev.next = cur.next
        return dummy.next
            
            



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    
        