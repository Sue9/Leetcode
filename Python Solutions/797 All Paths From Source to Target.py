# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:00:40 2018

@author: zhaoxu


797 All Paths From Source to Target
"""

class Solution(object):
    """
    def allPathsSourceTarget(self, graph):
        
    
        return self.dfs(0, len(graph)-1, graph)
     """   
    """
    def dfs(self, pos, end, graph):
        
        if pos == end:
            return [[]]
        
        
        path = []
#        visited = [pos]
        for i in graph[pos]:
#            visited.append(i)
            visited = [i]
            if end == i:
                return [visited]
            
            
            tmpL = self.dfs(pos+1, end, graph)
            
            for j in range(len(tmpL)):
                path.append(visited + tmpL[j])
#            visited.remove(i)
            
        return path
    """
        
        
        
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(graph, res, 0, [0])
        return res


    def dfs(self, graph, res, pos, path):
        if pos == len(graph) - 1:
            res.append(path)
            return
        else:
            for n in graph[pos]:
                self.dfs(graph, res, n, path + [n])
