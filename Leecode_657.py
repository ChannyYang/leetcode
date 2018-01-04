# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:14:35 2017

@author: tpp05624
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        R=0
        L=0
        U=0
        D=0
        for digit in moves:
            if digit=='R':
                R=R+1
                L=L-1
            elif digit=='L':
                L=L+1
                R=R-1
            elif digit=='D':
                D=D+1
                U=U-1
            elif digit=='U':
                U=U+1
                D=D-1
        if R==L==U==D==0:
            return True
        else:
            return False