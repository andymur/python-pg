#!/usr/bin/python3


import math
import os
import random
import re
import sys

def permute(l):
    for i in range(len(l) - 1):
        j = i + 1
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
            return (l[j], l)
    return (None, l)

def solution(l, deb = False):
    d = [0 for x in range(len(l))]
    el, l = permute(l)
    while el:
        d[el - 1] += 1
        if any(map(lambda x: x > 2, d)):
            return "Too chaotic"
        el, l = permute(l)
        if deb:
            print(el, l, d)
    if deb:
        print(d)
    if any(map(lambda x: x > 2, d)):
        return "Too chaotic"
    return sum(list(filter(lambda x: x > 0, d)))

# Complete the minimumBribes function below.
def minimumBribes(q):
    return solution(q)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
