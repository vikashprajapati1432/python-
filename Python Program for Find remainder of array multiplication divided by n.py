# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:15:33 2022

@author: ugly
"""

#to use reduce function import reduce from functools

from functools import reduce

def find_remainder(arr,n):

#use the reduce function to calculate sum

   sum_1=reduce(lambda x,y: x*y,arr)
   print(sum_1)
   remainder=sum_1%n
   
   print(remainder)

arr=[1,2,3,4,5]
print(arr)
n=6

find_remainder(arr,n)
