# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:47:55 2019

@author: Sue

328. Odd Even Linked List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head is None) or (head.next is None):
            return head
        
        #head had at least one elements
        podd = head
        even = peven = head.next
        
        while (peven.next and peven.next.next):
            
            podd.next = podd.next.next
            podd = podd.next
            
            peven.next = peven.next.next
            peven = peven.next
                    
        if(peven.next):
            podd.next = peven.next
            podd = podd.next
            peven.next = None
            
        podd.next = even
        
        return head
            
        