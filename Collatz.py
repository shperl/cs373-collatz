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
    high = int(max(i, j))
    low = int(min(i, j))
    global lazy_cache

    interval = range(low, high+1)
    most = 0

    for num in interval:
        current = collatz_cycles(num)
        current = lazy_cache[num]
        if current > most:
            most = current

    return most

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
            temp = temp >> 1
            cycles+=1
        else:
            temp += (temp << 1) + 1
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
