# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""

#!/usr/bin/env python3

# START

q0 = 0

f = {0, 4, 7}

def delta(q, a):
    if q == 0:
        if a == 'a':
            return {1}
        elif a =='l':
            return {2}
        else:
            return {0}
    elif q == 1:
        if a == 'a':
            return {0}
        elif a == 'l':
            return {5}
        else:
            return {1}
    elif q == 2:
        if a == 'a':
            return {1}
        elif a=='g':
            return {3}
        else:
            return {0}
    elif q == 3:
        if a == 'a':
            return {1}
        elif a == 'p':
            return {4}
        else:
            return {0}
    elif q == 4:
        if a == 'a':
            return {1}
        else:
            return {4}
    elif q == 5:
        if a=='a':
            return {0}
        elif a=='g':
            return {6}
        else:
            return {1}
    elif q == 6:
        if a=='a':
            return {0}
        elif a=='p':
            return {7}
        else:
            return {1}
    else:
         if a == 'a':
             return {0}
         else:
             return {7}

# END

def recognize(word):
    qs = set([q0])
    for a in word:
        qs_prime = set()
        for q in qs:
            qs_prime.update(delta(q, a))
        qs = qs_prime
    return f.intersection(qs)

def main(args):
    word = args[1]
    if recognize(word):
        print('word accepted')
    else:
        print('word NOT accepted')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))