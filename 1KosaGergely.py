# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""
import sys

text = sys.argv[1]
example = str(sys.argv[2])

def SS(text,example):
    with open(text) as f:
        szoveg=f.read().strip()
        # szoveg=eszoveg.replace(" ", "")
        m=len(example)
        n=len(szoveg)
        x=0
        talalat=-1
        for i in range(n-m+1): 
            a=0
            while a<m and szoveg[i+a]==example[a]:
                    a+=1
                    x+=1
            if a==m:
                talalat=i+1
                oh=x+i
        
    if talalat==-1:
        print(f"Gyorskeresés: {oh:>5} összehasonlítással, nincs találat")
     
    else:
        print(f"Gyorskeresés: {oh:>5} összehasonlítással, a találat helye: {talalat:>4}")

text = sys.argv[1]
pattern = str(sys.argv[2])

def QS(text,pattern):
    with open(text) as f:
        text=f.read().strip()
    m=len(pattern)
    n=len(text)
    minta=list(pattern)
    szoveg=list(text)
    uf=[]
    forditott=minta.copy()
    forditott.reverse()
    for i in range(m):
        uf.append(i+1)
        
    talalat=-1
    k=0 #eltolas
    m1=0
    oh=0 #osszehasonlitas
    while m1<m:
        if k>n-m:
            break
        if szoveg[k+m1]==minta[m1]:
            m1+=1
            oh+=1
        else:
            oh+=1
            if szoveg[k+m] in forditott:
                k+=uf[forditott.index(szoveg[k+m])]
            else:
                k+=m+1
                m1=0
        if m1==m:
            talalat=k+1
            break
    if talalat==-1:
        print(f"Gyorskeresés: {oh:>5} összehasonlítással, nincs találat")
     
    else:
        print(f"Gyorskeresés: {oh:>5} összehasonlítással, a találat helye: {talalat:>4}")
            
            
                







                    
            
        
        
    