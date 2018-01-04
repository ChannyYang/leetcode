# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:30:05 2017

@author: tpp05624
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""

def matrixReshape(nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        #rows=len(nums)
        #columns=len(nums[0])
        newnums=list()
        newnum=list()
        if len(nums)*len(nums[0])==r*c:
            totalc=0
            for num in nums:
                for i in num:
                    newnum.append(i)
                    totalc=totalc+1
                    if totalc==c:
                        newnums.append(newnum)
                        totalc=0
                        newnum=list()
            
            return newnums       
        else:
            return nums
            
print(matrixReshape([[1,2],[3,4]], 4, 1))
