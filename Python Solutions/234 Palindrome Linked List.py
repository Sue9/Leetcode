# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:19:35 2019

@author: Sue

234. Palindrome Linked List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
     
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        while(head):
            stack.append(head.val)
            head = head.next
            
        return (stack == stack[::-1])
