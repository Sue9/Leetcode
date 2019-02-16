# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:59:03 2019

@author: Sue

155. Min Stack
"""

class MinStack(object):

    #Way 2
    def __init__(self):
        """
        initialize your data structure here.
        """
        #left to right : bottom to top
        self.stack = []
        self.size = 0
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.size += 1
        if(self.min is None):
            self.min = x
        elif(self.min > x):
            self.min = x
        

    def pop(self):
        """
        :rtype: void
        """
        if(self.size == 0):
            return
        else:
            if(self.min == self.stack[-1]):
                self.min = self.stack[0]
                for i in self.stack[1:(self.size - 1)]:
                    if(i < self.min):
                        self.min = i
            
            self.stack = self.stack[:(self.size - 1)]
            self.size -= 1
            
        
        

    def top(self):
        """
        :rtype: int
        """
        if(self.size == 0):
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
    
    
    """
    #Way 1
    
    def __init__(self):
        
        #left to right : bottom to top
        self.stack = []
        self.size = 0

    def push(self, x):
        
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        
        if(self.size == 0):
            return
        else:
            self.stack = self.stack[:(self.size - 1)]
            self.size -= 1
        
        

    def top(self):
        
        if(self.size == 0):
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        
        if(self.size == 0):
            return None
        else:       
            return min(self.stack)
        
    """   


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

