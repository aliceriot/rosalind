#!/usr/bin/python

#quick algo (memoized) to calculate fibonacci numbers

def fibo(n):
    if n == 0:
        return 0
    fiblist = range(0,n+1)
    for i in fiblist:
        if i == 0 or i == 1:
            pass
        else:
            fiblist[i] = fiblist[i-1] + fiblist[i-2]
    return fiblist[n]

