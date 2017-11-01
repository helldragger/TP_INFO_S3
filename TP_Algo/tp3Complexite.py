# -*- coding:utf-8 -*-

# psyco est un module basé sur les techniques de "compilation à la volée"
# et permet ainsi d'accélérer l'exécution des programmes.
try:
    import psyco
    psyco.full() 
except:
    pass

from random import randrange
from time import time

c_s = 0
c_f = 0
c_r = 0

def tirageAleatoire(taille,rang=30):
    """retourne un tableau de taille entiers dont les valeurs
    sont tirées aléatoirement dans l'intervalle [0,rang-1]"""
    res=[0]*taille
    for i in range(taille):
        res[i]=randrange(rang)
    return res

###########################   TRI RAPIDE   ###########################

def partition(tableau,g,d):
    "partition du tableau dans l'intervalle [g,d]"
    global c_r
    pivot=tableau[g]
    courg=g+1  
    courd=d 
    while True:
        while courg<d and tableau[courg]<=pivot:
            c_r += 1
            courg=courg+1
        while tableau[courd]>pivot:
            c_r += 1
            courd=courd-1
        if courg < courd:
            tableau[courg],tableau[courd]=tableau[courd],tableau[courg]
        else:
            tableau[g],tableau[courd]=tableau[courd],tableau[g]
            return courd

def triRapide(tableau,g,d):
    "tri du tableau dans l'intervalle [g,d], donc tri de tableau[g:d+1]"
    if g<d:
        i=randrange(g,d+1)
        tableau[g],tableau[i]=tableau[i],tableau[g]
        m=partition(tableau,g,d)
        triRapide(tableau,g,m-1)
        triRapide(tableau,m+1,d)

print("Un exemple d'execution de triRapide:"); print
L=[5,3,4,7,4,1]; print("la liste initiale:", L)
print
triRapide(L,0,5); print("la meme liste, mais triee:", L)

##########################   TRI SELECTION   #########################

## 1) Ecrire la fonction TriSelection

def triSelection(tableau):
    global c_s

    for done in range(len(tableau)):
        min = tableau[done]
        for i in range(done, len(tableau)):
            c_s += 1
            if tableau[i] < min:
                min = i
        temp = tableau[done]
        tableau[done] = tableau[min]
        tableau[min] = temp
    return tableau


##########################   TRI FUSION   #########################

## 2) Ecrire la fonction fusion

def fusion(tab1,tab2):
    """ retourne le tableau résultant de la fusion
    des deux tableaux triés tab1 et tab2 """
    
    res=[]
    # à compléter
    i,j=0,0
    global c_f

    while not (i == len(tab1) and j == len(tab2)):
        if i == len(tab1): #liste 1 finie
            res.append(tab2[j])
            j += 1
        elif j == len(tab2):#liste 2 finie
            res.append(tab1[i])
            i += 1
        else:
            c_f += 1
            if tab1[i] <= tab2[j]:
                res.append(tab1[i])
                i += 1
            else:
                res.append(tab2[j])
                j += 1
    return res


def triFusion(tableau,g,d):
    if g<d:
        m=(g+d)//2
        triFusion(tableau,g,m)
        triFusion(tableau,m+1,d)
        tableau[g:d+1]=fusion(tableau[g:m+1],tableau[m+1:d+1])


##########################   TEST   #########################                

## 3) Tester les temps d'exécution des différents tris
##        pour différentes tailles: 10, 100, 1000,
##        et, si on peut: 10 000, 100 000, 1 000 0000
        
def test(n):
    monTab=tirageAleatoire(n,n)
    print("*"*20); print("taille = "),; print(n)
    tonTab=monTab[:]

    global c_r
    global c_f
    global c_s

    c_r = 0

    t1=time()
    triRapide(tonTab,0,len(tonTab)-1)
    t2=time()
    print("temps du tri rapide: "); print(t2-t1)
    print("nb comparaisons:", c_r)

    c_s = 0

    t1=time()
    triSelection(tonTab)
    t2=time()
    print("temps du tri selection: "); print(t2-t1)
    print("nb comparaisons:", c_s)

    c_f = 0

    t1=time()
    triFusion(tonTab,0,len(tonTab)-1)
    t2=time()
    print("temps du tri fusion: "); print(t2-t1)
    print("nb comparaisons:", c_f)


for el in [10,100,1000,10000,100000,1000000]:

    test(el)


## 4) Pour chacun des tris, introduire une variable compteur (globale)
##      pour compter le nombre de comparaisons entre paires d'éléments du tableau.
##
##    Pour chacun des tris, répondre à la question suivante:
##    Quand on multiplie la taille par 10, par combien est multiplié le temps? le nombre de comparaisons?

# selection: n*10 => O(s) = n²/2
# = (10*n)²/2 = 100n²/2
# multiplier n par 10 reviens a ralentir = 100 * O(selection)

# fusion : n*10 => O(f) = nlog(n) => (10n)log(10n)
# = (10n)*(log(n)+log(10))
# = 10nlog(n) + 10nlog(10)
# = 10( nlog(n) + nlog(10))
# multiplier n par 10 reviens a ralentir ~= 10 * O(fusion) + nlog(10)

# pareil pour le rapide : n*10 => O(r) = (n+10)log(n+10)
# = (10n)*(log(n)+log(10))
# = 10nlog(n) + 10nlog(10)
# = 10( nlog(n) + nlog(10))
# multiplier n par 10 reviens a ralentir ~= 10 * O(rapide) + nlog(10)


# le temps augmente autant que le nombre de comparaisons pour le selection
# mais pas pour le fusion et le rapide qui ont d'autres étapes plus complexes
# le fusion, le rapide est legerement plus lent que le fusion a cause des
# iterations pour trouver les pivots.


# questions
# 1) ( n**2 )/2

# 2) (n/2)**2+n => n²/4 +n => n * ( n/4 +1)

