# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""

class Nyelvtan:
    """
    CF nyelvtant reprezentáló osztály.
    """

    def __init__(self, kezdovaltozo):
        """
        Inicializál egy új Nyelvtan objektumot.

        :param kezdovaltozo: A nyelvtan kezdőváltozója, az egyik 
                             nemterminális.
        """

        if not nemterminalis(kezdovaltozo):
            raise ValueError("A kezdőváltozó nemterminális kell legyen")

        self._kezdovaltozo = kezdovaltozo
        # TODO Itt lehet inicializálni a szabályokat tároló adatstruktúrát.
        self.szabalyok={}

    def add_szabaly(self, bal, jobb):
        """
        Új levezetési szabályt ad a nyelvtanhoz.

        :param bal: A szabály bal oldala, egy nemterminális szimbólum.
        :param jobb: Terminális és nemterminális szimbólumok sztringje,
                     vagy ilyen sztringek listája.
        """

        if not nemterminalis(bal):
            raise ValueError("Szabály bal oldalán csak egy nemterminális állhat")

        # TODO Vegyük fel a szabályt a nyelvtanba.
        if bal not in self.szabalyok:
            if type(jobb)==list:
                self.szabalyok[bal]=jobb
            else:
                self.szabalyok[bal]=[jobb]
        else:
            if type(jobb)==list:
                self.szabalyok[bal].extend(jobb)
            else:
                self.szabalyok[bal].append(jobb)
    def levezet(self, szo):
        """
        Megkeres egy bal-levezetést a megadott szóhoz.

        :param szo: A levezetendő szó.
        :return: A levezetési lépések listája, vagy `False`, 
                 ha nem található levezetés. 
        """

        if not szo.islower():
            raise ValueError("A levezetendő szó nem tartalmazhat nemterminálist")

        return self._szelessegi_keres(self._kezdovaltozo, szo)

    def _szelessegi_keres(self, honnan, hova):
        """
        Szélességi kereséssel utat keres a `honnan` es `hova` csúcsok között.

        :param honnan: A kiindulási csúcs, terminálisok és 
                       nemterminálisok sztringje.
        :param hova:   A célcsúcs, terminálisok és nemterminálisok sztringje.
        :return:       Az út csúcsainak listája, vagy `False`, 
                       ha nem található levezetés.
        """
        szulo = {}
        sor = [honnan]

        while hova not in szulo:
            if not sor:
                return False
            csucs = sor.pop(0)
            for gyerek in self._rakovetkezo(csucs):
                if gyerek not in szulo and gyerek != honnan:
                    szulo[gyerek] = csucs
                    sor.append(gyerek)

        return utat_kiolvas(szulo, honnan, hova)

    def _rakovetkezo(self, csucs):
        """
        Megadja a `csucs`-ból kimenő élen elérhető csúcsok listáját.

        :param csucs: A forrás csúcs, terminálisok és nemterminálisok 
                      sztringje.
        :return:      A `csucs` sztringből bal-levezetési lépésekkel 
                      elérhető sztringek listája.
        """

        # TODO Keressük meg a rákövetkező szavakat.
        if csucs.islower():
            return[csucs]
        for i in csucs:
            if i.isupper():
                return [csucs.replace(i, j, 1) for j in self.szabalyok[i]]

def nemterminalis(s):
    """
    :param s: A megvizsgálandó sztring.
    :return: `True`, ha az `s` egy nemterminális szimbólum.
    """

    return len(s) == 1 and s.isupper()

def utat_kiolvas(szulo, honnan, hova):
    """
    Megad egy utat a `honnan` és a `hova` csúcs között a szélességi fában.

    :param szulo: A csúcsok szülőit tartalmazó szótár (dictionary).
    :param honnan: Az út kezdőpontja.
    :param hova: Az út végpontja.
    :return: A kiolvasott út csúcsainak listája, ami lehet üres.
    """

    ut = []
    if hova not in szulo:
        return ut
    csucs = hova

    while csucs != honnan:
        ut.append(csucs)
        csucs = szulo[csucs]

    ut.append(honnan)
    ut.reverse()
    return ut

if __name__ == '__main__':
    import sys

    g = Nyelvtan("S")
    g.add_szabaly("S", ["XSX", "R"])
    g.add_szabaly("R", ["aTb", "bTa"])
    g.add_szabaly("T", ["XTX", "X", ""])
    g.add_szabaly("X", "a")
    g.add_szabaly("X", "b")

    levezetes = g.levezet(sys.argv[1])
    if levezetes:
        print(" => ".join(levezetes))
    else:
        print("Nincs levezetés")
        