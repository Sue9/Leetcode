# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:12:48 2019

@author: Sue

817. Linked List Components
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        #try to use head.next instead flag
        cnt = 0
        
        while(head):
            if(head.val in G) and (head.next is None or head.next.val not in G):
                cnt += 1
            head = head.next
        return cnt
        
        """
        #using Dictionary
        dictG = {}
        while(G):
            if(dictG.__contains__(G[0])):
                dictG[G[0]] += 1
            else:
                dictG[G[0]] = 1
            G = G[1:] 
        
        cnt = 0
        flag = False
        while(head):
            if (dictG.__contains__(head.val) and flag == False):
                cnt += 1
                flag = True
            elif (not dictG.__contains__(head.val)):
                flag = False
            head = head.next
        return cnt
        """
    
        """
        cnt = 0
        flag = False
        while(head):
            if (head.val in G and flag == False):
                cnt += 1
                flag = True
            elif (head.val not in G):
                flag = False
            head = head.next
        return cnt
        """
            
                
            
        