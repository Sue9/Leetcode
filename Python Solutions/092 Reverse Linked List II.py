# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:22:00 2019

@author: Sue

092. Reverse Linked List II
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseToN(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(n <= 1):
            return head
        
        prev = head
        m = n
        print("Find Tail")
        while (m >= 1):
            print("prev.val = ", prev.val)
            prev = prev.next
            m -= 1
                
        cur = head
        print("Reverse Start")
        while (n >= 1):
            print("cur.val = ",cur.val)
            tail = cur.next
            cur.next = prev
            prev = cur
            cur = tail
            n -= 1
        
        return prev
        
    
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if(m >= n):
            return head
        
        if(m == 1):
            return self.reverseToN(head, n)
        #m<n
        prev = ListNode(None)
        prev.next = head
        
        
        while(m > 1):
            prev = prev.next
            m -= 1
            n -= 1
        prev.next = self.reverseToN(prev.next, n)
        return head
        
