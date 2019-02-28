# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:52:53 2019

@author: Sue

2. Add Two Numbers
"""
def printListNode(head):
    s = ""
    while(head):
        s += str(head.val) + " -> "
        head = head.next
    s += "NULL"
    return s
        
def createListNode(arr):
    if(arr == []):
        return ListNode(None)
        
    res = ListNode(arr[0])
    head = res
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
    return res


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur = res = ListNode(0)
        
        while(l1 and l2):
            s = l1.val + l2.val + carry
            carry = 0
            if(s >= 10):
                s -= 10
                carry = 1
             
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        if(l1 is not None):
            while (l1):
                s = l1.val + carry
                carry = 0
                if(s >= 10):
                    s -= 10
                    carry = 1
                cur.next = ListNode(s)
                cur = cur.next
                
                l1 = l1.next
        elif(l2 is not None):
            while (l2):
                s = l2.val + carry
                carry = 0
                if(s >= 10):
                    s -= 10
                    carry = 1
                cur.next = ListNode(s)
                cur = cur.next
                
                l2 = l2.next
         # l1 is None and l2 is None
        if carry:
            cur.next = ListNode(carry)
            
        return res.next
            
            
            