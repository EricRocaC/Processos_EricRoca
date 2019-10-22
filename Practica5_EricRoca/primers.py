#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys;

class llista_primers:
    """
    Creem una llista per a afegir-hi els nombres primers començant per el dos
    i sumant-li continuament fins a un màxim de números demanats per l'usuari.
    >>> llista_primers(5).l
    """
    def __init__(self, n):
        """inicialitzem la variable n i creem la llista buida i el buscador."""
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        Dins d'aquest apartat ens dedicarem a treballar amb els ifs.
        El primer if afegirà un 2 dins de la llista buida.
        El segón comprobarà si la llista és més petita que el número introduit per l'usuari i donarà pas al bucle.
        El while comprobarà si "trobat" és "false" (cas que es donará, com deiem abans, quan la llista sigui igual al número introduit).
        El for farà un "mod" comprobant que el residu entre el número que estem utilitzant i l'últim a la llista sigui 0.
        Si ho es, l'afegirà a la llista. Un com acabada la llista, el programa sortirà del bucle i acabarà.
        """
        if (len(self.llista) == 0):
            #si la llista continua buida, aquest if li afegira un 2 com a primer parametre de la llista.
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            #mentre llista sigui més petit que n (que es el número que l'usuari li ha introduit) trobat serà False...
            trobat = False
            #... i es sumara 1 al últim número de la llista.
            seguent = self.llista[-1]+1
            while not trobat:
                #mentre trobat sigui false el bucle seguirà actiu.
                for i in self.llista:
                    #fem un "seguent" mod "i" per a buscar un número que dividit entre algún els números que tenim a la llista doni residu 0.
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                    #Un cop a la llista tenim tots els números que ens demanaba l'usuari trobat serà true i tencarà el bucle.
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    l = llista_primers(int(sys.argv[1]))
    print l.llista