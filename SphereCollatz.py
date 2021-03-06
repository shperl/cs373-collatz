#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

lazy_cache = [0] * 1000000

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    interval = range(i, int(j)+1)
    max = 0

    for num in interval:
        current = collatz_cycles(num)
        if current > max:
            max = current

    return max

# -------------
# collatz_cycles
# -------------

def collatz_cycles (i):
    """
    i is the integer value we are counting cycles for
    return the cycle length of that number
    """
    global lazy_cache
    cycles = 1
    temp = i


    if lazy_cache[i] > 0:
        return lazy_cache[i]

    while temp > 1:
        
        assert cycles > 0
        if temp % 2 == 0:
            temp = temp / 2
            cycles+=1
        else:
            temp = (3 * temp) + 1
            cycles+=1

    lazy_cache[i] = cycles
    
    return cycles

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)


# ----
# main
# ----

if __name__ == "__main__" : # pragma no cover
    collatz_solve(sys.stdin, sys.stdout)

""" # pragma no cover
% cat RunCollatz.in
1 10
100 200
201 210
900 1000
1000 2501
1000 1001
2000 11005
3000 21009
4000 31013
5000 41017
6000 51021
7000 61025
8000 71029
9000 81033
10000 91037
11000 101041



% SphereCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 20
100 200 125
201 210 89
900 1000 174
1000 2501 209
1000 1001 143
2000 11005 268
3000 21009 279
4000 31013 308
5000 41017 324
6000 51021 324
7000 61025 340
8000 71029 340
9000 81033 351
10000 91037 351
11000 101041 351



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
