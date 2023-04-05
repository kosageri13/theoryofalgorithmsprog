# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""
def grafot_olvas(f):
    """
    Beolvassa a gráfot egy szöveges fájlból.

    :param f: A beolvasandó fájl.
    :return:  A gráf éllistája, az út kezdő- és végpontja.
    """

    fejlec = f.readline().split()
    n, m, honnan, hova = [int(s) for s in fejlec]

    graf = dict((i, []) for i in range(n))
    for j in range(m):
        el = f.readline().split()
        u, v = [int(s) for s in el]
        graf[u].append(v)

    return graf, honnan, hova

def utat_keres(graf, honnan, hova):
    """
    Megkeres egy legrövidebb utat a gráf két csúcsa között.

    :param graf: A gráf éllistája.
    :param honnan: Az út kezdőpontja.
    :param hova: Az út végpontja.
    :return: Egy legrövidebb út csúcsainak listája, 
             ha létezik út, egyébként False.
    """

    # TODO Itt valósítsuk meg a szélességi keresést.
    szulo={}    
    a=[honnan]
    values=[]
    if honnan==hova:
        szulo[hova]=honnan
        return utat_kiolvas(szulo, honnan, hova)
    for key in graf:
        if key==a[0]:
            values=graf[key]
            for i in values:  
                if i not in szulo:
                    a.append(i)
                    szulo[i]=key
                    del a[0]
                if i==hova:
                    return utat_kiolvas(szulo, honnan, hova)
    while a:
        for key in graf:
            if key==a[0]:
                values=graf[key]
                for i in values:  
                    if i not in szulo:
                        a.append(i)
                        szulo[i]=key
                        del a[0]
                    if i==hova:
                        return utat_kiolvas(szulo, honnan, hova)

def utat_kiolvas(szulo, honnan, hova):
    """
    Megad egy utat a honnan és a hova csúcs között a szélességi fában.

    :param szulo: A csúcsok szülőit tartalmazó szótár (dictionary).
    :param honnan: Az út kezdőpontja.
    :param hova: Az út végpontja.
    :return: A kiolvasott út csúcsainak listája, ha létezik út,
             egyébként False.
    """

    if hova not in szulo:
        return False

    ut = []
    csucs = hova

    while csucs != honnan:
        ut.append(csucs)
        csucs = szulo[csucs]

    ut.append(honnan)
    ut.reverse()
    return ut

if __name__ == '__main__':

    import sys

    with open(sys.argv[1], 'r') as f:
        graf, honnan, hova = grafot_olvas(f)
    ut = utat_keres(graf, honnan, hova)

    if ut:
        print('Van út: ' + ' -> '.join(str(i) for i in ut))
    else:
        print('Nincs út')
