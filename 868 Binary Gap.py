# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:23:09 2018

@author: zhaoxu



"""

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        res, last = 0, None  # res 保存结果， last 记录上个一个1出现的位置。
        for i in range(32):
            print (i, " : N = ", N , " res = " , res, " last = ", last)
            if (N >> i) & 1:
                print("    in if-loop: " )
                print("\t\t N>>i = ", N>>i)
                print("\t\t res  = " , res)
                print("\t\t last =" , last)
                if last is not None:  # 现在的 i，表示1 出现的位置
                    res = max(res, i - last)  # 更新结果
                    print("\t\t\t\t two ifs: ")
                    print("\t\t\t\t i-last = " , i - last)
                last = i
        return res
        
        
        """
        My solution
        
        bstr = bin(N)[2:]
        numOne = bstr.count('1')
        if( numOne ) <= 1:
            return 0
        
#        left = bstr.index('1')
        left = 0
        gaps = []
        for i in range(1, len(bstr) - bstr[::-1].index('1') , 1):
            if bstr[i] == '1':
                right = i
                gaps.append(right - left)
                left = i
                
        return max(gaps)
        """