# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:01:44 2017

@author: tpp05624
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard={'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'0':1,
              'Q':2,'W':2,'E':2,'R':2,'T':2,'Y':2,'U':2,'I':2,'O':2,'P':2,
              'A':3,'S':3,'D':3,'F':3,'G':3,'H':3,'J':3,'K':3,'L':3,
              'Z':4,'X':4,'C':4,'V':4,'B':4,'N':4,'M':4}
        matchlist=[]
        for word in words:
            flag=True
            dflag=keyboard[word[0].upper()]
            for digit in word[1:]:
                if dflag!=keyboard[digit.upper()]:
                    flag=False
                    break
            if flag:
                matchlist.append(word)
        return matchlist
                
#print(Solution.findWords(["Hello","Alaska","Dad","Peace"]))

