# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:48:22 2017

@author: tpp05624
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""

def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sdlist=[int]
        for i in range(left,right+1):
            flag=False
            for digit in str(i):
                if digit=='0':
                    flag=False
                    break
                elif i%int(digit)!=0:
                    flag=False
                    break
                else:
                    flag=True
               
            if flag:
                sdlist.append(i)
        return sdlist

def main():
    print(selfDividingNumbers(1,22))
if __name__ == "__main__":
	main()