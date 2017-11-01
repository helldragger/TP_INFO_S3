# coding:utf-8

# On utilise une classe pour définir le type pointeur sur noeud.
class Noeud(object):
    def __init__(self, val, suiv=None):
        """initialisateur de classe
        permet l'allocation de la mémoire requise pour stocker le noeud
        et l'initialisation de ses attributs val et suiv"""
        self.val = val
        self.suiv = suiv


# Quelques exemples de listes avec représentation simplement chaînée.
# a) la liste vide :
listeVide = None

# b) une liste réduite à l'élément 5 :
listeSingleton = Noeud(5)
# listeSingleton=Noeud(5) => appel de la fonction __init__ de Noeud
# avec comme paramètres : self=listeSingleton, val=5 et suiv=None
#
# Cette simple instruction correspond en pseudo-code à la séquence :
#     listeSingleton : pointeur sur noeud     # déclaration de type
#     Nouveau(listeSingleton)                 # allocation de la mémoire
#     listeSingleton->val=5                   # initialisation du champ val
#     listeSingleton->suiv=None               # initialisation du champ suiv


# c) la liste 2,5,8,10:


# Exo 1. A partir de la liste maliste=Noeud(2,Noeud(5,Noeud(8,Noeud(10))))
# écrivez l'instruction nécessaire pour afficher le 1er élément de maliste (l'élément 2)
# puis l'instruction nécessaire pour afficher le 3ème élément (ici 8).


def at_index(list, n):
    while n >= 0 and list is not None:
        if n == 0:
            return list.val
        list = list.suiv
        n -= 1
    return -1




# Exo 2. En utilisant les procédures données ci-dessous (essayez d'abord de bien les comprendre),
# écrivez les instructions nécessaires pour :
# a) afficher tous les éléments de maliste;
# b) ajouter l'élément 7 en début de maliste et afficher à nouveau maliste;
# c) ajouter l'élément 3 en fin de maliste et afficher à nouveau maliste;
# d) déterminer si l'élément 8 est ou non dans maliste.

def affiche(debut):
    while debut != None:
        print(debut.val, end=" "),
        debut = debut.suiv
    print("")


def insere_debut(debut, x):
    return Noeud(x, debut)


def insere_fin_it(debut, x):
    if debut == None:
        return Noeud(x)
    cour = debut
    while cour.suiv != None:
        cour = cour.suiv
    cour.suiv = Noeud(x)
    return debut


def recherche_rec(debut, x):
    if debut == None:
        return False
    if debut.val == x:
        return True
    return recherche_rec(debut.suiv, x)



# Exo 3. Donnez une version récursive de la procédure insere_fin(debut,x)
# qui prend en entrée deux arguments (debut qui est une référence
# sur le premier noeud d'une liste et x un élément)
# et qui insère x à la fin de la liste.

def ex3(l, n):
    if l is not None:
        l.suiv = ex3(l.suiv, n)
    else:
        return Noeud(n)
    return l


# Exo 4. Donnez une version itérative de la procédure recherche(debut,x)
# qui prend en entrée deux arguments (debut une référence
# sur le premier noeud d'une liste et x un élément) et
# qui détermine si x est ou non dans la liste.

def ex4(l, n):
    while l is not None:
        if l.val == n:
            return True
        l = l.suiv
    return False



# Exo 5. Écrivez une procédure inverse(debut)
# qui prend en entrée debut une référence sur le premier noeud d'une liste
# et qui retourne une référence sur le premier noeud de la liste inversée.

def ex5(l):
    first = None
    while l is not None:
        temp = Noeud(l.val)
        temp.suiv = first
        first = temp
        l = l.suiv
    return first



# Exo 6. Une liste L1 est une sous-liste d'une liste L2 si L1 est obtenue à partir de L2 en supprimant zéro, un ou plusieurs éléments de la liste L2.
# Exemple: la liste 3,5,10 est une sous-liste de la liste 2,3,5,5,7,10.
# Écrivez une procédure sousListe(L1,L2)
# qui prend en entrée deux listes L1 et L2 et qui retourne True si L1 est une sous-liste de L2.
# On supposera que L1 et L2 sont des listes d'entiers triés dans l'ordre croissant (au sens large).
def exo6(l_1, l_2):
    while l_1 is not None and l_2 is not None:
        if l_1.val == l_2.val:
            l_1 = l_1.suiv
        l_2 = l_2.suiv
    return l_1 is None



# Exos un peu plus difficiles (avec *):

# Exo 7. Écrivez une procédure insere_apres(L,x,y)
# qui insère un élément y après la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.

def exo7(l, x, n):
    node = l
    while node is not None:
        if node.val == x:
            temp = Noeud(n, node.suiv)
            node.suiv = temp
            return l
        node = node.suiv
    return l



# Exo 8. Écrivez une procédure insere_avant(L,x,y)
# qui insère un élément y avant la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.


def exo8(l, x, n):
    node = l
    previous = node
    while node is not None:
        if node.val == x:
            if previous == node:
                #Only happens when the first node is the occurence
                return Noeud(n, node)
            temp = Noeud(n, node)
            previous.suiv = temp
            return l
        previous = node
        node = node.suiv
    return l


## Test

#debut = None
#for i in range(3):
#    debut = insere_fin_it(debut, i)
#affiche(debut)

def main():
    maliste = Noeud(2, Noeud(5, Noeud(8, Noeud(10))))
    print("exo", 1)
    print(at_index(maliste, 2))
    print(at_index(maliste, 3))
    print("exo", 2)
    affiche(maliste)
    affiche(insere_debut(maliste, 7))
    affiche(insere_fin_it(maliste, 3))
    print(recherche_rec(maliste, 8))
    print("exo", 3)
    affiche(ex3(maliste, 2))
    print("exo", 4)
    print(ex4(maliste, 2))
    print(ex4(maliste, 4))
    print("exo", 5)
    affiche(ex5(maliste))
    print("exo", 6)
    print(exo6(maliste.suiv, maliste))
    print(exo6(maliste, maliste.suiv))
    print("exo", 7)
    affiche(exo7(maliste, 2, 1))
    print("exo", 8)
    affiche(exo8(maliste, 2, 1))

main()

