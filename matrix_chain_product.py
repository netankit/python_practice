#!/usr/bin/python
# -*- coding: UTF-8 -*-

def matrix_chain():
    #n = len(d) - 1
    n = 10
    N = [[0] *n for i in range(n)] 
    for b in range(1, n):
        print "loop 1"
        for i in range(n-b):
            j = i + b
            print b, i,j
            #N[i][j] = min(N[i][k]+N[k+1][j]+d[i] * d[k+1] * d[j+1] for k in range(i,j))
    return N



matrix_chain()