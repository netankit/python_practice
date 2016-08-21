#!/usr/bin/python
# -*- coding: UTF-8 -*-
import timeit

# rotate the array by k steps

arr = [1,2,3,4,5,6,7]
n =7
k = 3
# out: [5,6,7,1,2,3,4]


l = arr[k:]+ arr[0:k+1]


for i in reversed(l):
    print i
print l