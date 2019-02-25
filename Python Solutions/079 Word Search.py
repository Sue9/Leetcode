# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:18:30 2019

@author: Sue

079. Word Search
"""

class Solution(object):
    def __init__(self):
        self.dir = [[-1, 0], # Up
                    [0, 1],  # Right
                    [1, 0],  # Down 
                    [0, -1]  # Left
                    ]
    
    def inArea(self, row, col, x, y):
        if (x >= 0) and (x < row) and (y >= 0) and (y < col):
            return True
        return False
    
    
    def searchAdjacent(self, board, word, visited, x, y):
        """
        :type board: List[List[str]]
        :type word: str : left string to be searched
        :type visited: List[bool] : if the position is visited
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        #All char in word has been found in the board
        if (word == ""):
            return True
        
        #Else, search
        row = len(board)
        if( row == 0 ):
            return False
        col = len(board[0])
                
        if(word[0] == board[x][y]):
            if (len(word[1:]) == 0):
                return True
            
            visited[x][y] = True
            
            #continune searching
            for d in self.dir:
                newX = x + d[0]
                newY = y + d[1]
                
                if (self.inArea(row, col, newX, newY)) and (not visited[newX][newY]):            
                    if (self.searchAdjacent(board, word[1:], visited, newX, newY)):
                        return True
                    else:
                        visited[newX][newY] = False  
                        continue
                    
        else:
            return False
        
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #if the word is empty, then return true
        if(word == ""):
            return True
        
        row = len(board)
        if( row == 0 ):
            return False
        
        col = len(board[0])        
            
        for x in range(row):
            for y in range(col):
                visited = [[False] * col for i in range(row)] 
                
                res = self.searchAdjacent(board, word, visited, x, y)
                if (res):
                    return True
                
        return False
        
        
