#!/usr/bin/python
# -*- coding: UTF-8 -*-

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        # print ("left half", lefthalf)
        righthalf = alist[mid:]
        # print ("right half", righthalf)
        # print "one .. "
        mergeSort(lefthalf)
        # print "two .. "
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            # print "first"
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        # print ("after first : ", alist)
        while i < len(lefthalf):
            # print "second"
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # print ("after Second : ", alist)
        while j < len(righthalf):
            # print "third"
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        # print ("after third : ", alist)
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
