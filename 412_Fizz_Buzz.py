# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:03:32 2017

@author: tpp05624
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzlist=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5!=0:
                    fizzBuzzlist.append("Fizz")
                else:
                    fizzBuzzlist.append("FizzBuzz")
            elif i%5==0:
                fizzBuzzlist.append("Buzz")
            else:
                fizzBuzzlist.append(str(i))
        return fizzBuzzlist
    
print(fizzBuzz(15))
def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]