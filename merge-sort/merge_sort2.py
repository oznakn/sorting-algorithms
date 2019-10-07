#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:03:06 2019

@author: drewgilliesbc
"""
from time import perf_counter

#array to be sorted
Array = [99,21,19,22,28,11,14,18, 70]
 
#start performance start time
start = perf_counter()
#function for merging two sub-arrays
def merge(left, right, Array):
  i = 0
  j = 0
  k = 0
 
  while (i<len(left) and j<len(right)):
    if(left[i]<right[j]):
      Array[k] = left[i]
      i = i+1
    else:
      Array[k] = right[j]
      j = j+1
 
    k = k+1
  
  while(i<len(left)):
    Array[k] = left[i]
    i = i+1
    k = k+1
  
  while(j<len(right)):
    Array[k] = right[j]
    j = j+1
    k = k+1
 
#function for dividing and calling merge function
def mergesort(Array):
  n = len(Array)
  if(n<2):
    return
 
  mid = n//2
  left = Array[0:mid]
  right = Array[mid:n]

 
  mergesort(left)
  mergesort(right)
 
  merge(left,right,Array)
 
#calling mergesort
mergesort(Array)
for i in Array:
  print (i)
# end time
end = perf_counter()
print('sorting took ',end - start)
