# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:59:41 2017

@author: tpp05624
"""

def calPoints(ops):
    
        """
        :type ops: List[str]
        :rtype: int
        """
        scorelist=[]
        for digit in ops:
          
            if digit=='C':
        
                scorelist.pop(-1)
            elif digit=='D':
        
                scorelist.append(scorelist[-1]*2)
            elif digit=='+':
        
                scorelist.append(scorelist[-1]+scorelist[-2])
            else:
                scorelist.append(int(digit))
        return sum(scorelist)

print(calPoints(["5","2","C","D","+"]))                