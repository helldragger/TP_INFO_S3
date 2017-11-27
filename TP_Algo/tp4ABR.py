# -*- coding:utf-8 -*-

######################    Arbre Binaire de Recherche (ABR)   ######################

class Noeud(object): 
  def __init__(self, element, ga=None, dr=None): 
    self.val = element 
    self.ga  = ga
    self.dr = dr


def voir(A,dec=1):
    "un affichage planaire de l'arbre binaire A modulo une rotation à 90°"
    if A == None:return ""
    return voir(A.dr,dec+5)+' '*dec+str(A.val)+'\n'+voir(A.ga,dec+5)


# 1. Écrivez une procédure minimum(A) qui retourne un pointeur sur le noeud de valeur minimale d'un ABR A
#    (et retourne None si l'ABR est vide).
import math
def minimum(A):
    if A is None:
        return None
    if A.ga is not None:
        return minimum(A.ga)
    return A


# 2. Écrivez une procédure itérative present(A,x) qui, étant donné un ABR A
# et un élément x,
#    détermine si l'élément x est présent ou non dans l'ABR A (la procédure retourne un booléen).
def present(A, x):
    while A is not None: # is not est plus rapide, sécu et propre que !=

        # != est un test d'égalité, ce qui veut dire que python va chercher
        #  la fonction __equals__ de l'objet a comparer, et cela peut poser
        # probleme si l'objet en lui meme as une fonction equals lente et qui
        #  ne retourne pas faux directement face à none.

        # is not est un test d'identité, None en python est un singleton
        # constant, la comparaison est instantanée car elle vérifie juste si
        # les deux valeurs sont bien stockées au même endroit. Ceci evite les
        #  fonctions equals et les risques de comparaisons avec des erreurs.
        if x > A.val:
            A = A.dr
        elif x < A.val:
            A = A.ga
        else:
            return True
    return False

# 3. Écrivez une procédure insere(A,x) qui renvoie l'ABR A où on a ajouté l'élément x.
#    La procédure ne modifie rien si x est déjà dans A.
def insere(A, x):
    node = A
    while node is not None:
        if x > node.val:
            if node.dr is not None:
                node = node.dr
            else:
                node.dr = Noeud(x)
                return A
        elif x < node.val:
            if node.ga is not None:
                node = node.ga
            else:
                node.ga = Noeud(x)
                return A
        else:
            return A




# 4. Écrivez une procédure affiche(A) qui affiche tous les éléments d'un ABR A
#    dans l'ordre croissant.
def affiche(A):
    if A is not None:
        affiche(A.ga)
        print(A.val)
        affiche(A.dr)


# # 5*. Écrivez une procédure afficheIntervalle(A,debut,fin)
#    qui, pour deux valeurs debut et fin supposées telles que début <= fin,
#    affiche tous les éléments x de l'ABR A qui appartiennent à l'intervalle [debut, fin].
#    Évitez les parcours de sous-arbres inutiles.
def afficheIntervalle(A, debut, fin):
    if A is not None:
        if fin < A.val:
            afficheIntervalle(A.ga, debut, fin)
        elif A.val < debut:
            afficheIntervalle(A.dr, debut, fin)
        elif debut <= A.val <= fin:
            afficheIntervalle(A.ga, debut, A.val)
            print(A.val, end=" ")
            afficheIntervalle(A.dr, A.val, fin)


#    Considérez les 4 cas suivants:
#    1) A = None : rien à afficher;
#    2) fin < A.val : appel récursif sur le sous-arbre gauche;
#    3) A.val < debut : appel récursif sur le sous-arbre droit;
#    4) debut <= A.val <= fin :
#     appel récursif sur le sous-arbre gauche et l'intervalle [debut,A.val], écrire A.val
#     puis appel récursif sur le sous-arbre droit et l'intervalle [A.val,fin]

# 6**. Écrivez une procédure rechercheKeme(A,k)
#    qui recherche le k-ème plus petit élément de l'ABR A, pour k>=1.
#
#    Le principe est d'effectuer un parcours infixé où
#    l'on décrémente k lors de la visite de chaque noeud.
#
#    Cette procédure retourne un couple: un élément et un entier.
#
#    Dans le cas où ce k-ème plus petit élément de A existe (k <= taille de l'ABR A),
#    l'élément correspond au k-ème plus petit élément de l'ABR A
#    et l'entier vaut 0.
#
#    Dans le cas où ce k-ème plus petit élément n'existe pas,
#    on donne à l'élément une valeur 'bidon', -1 par exemple,
#    et l'entier vaut k moins le nombre d'éléments de l'ABR A.


def rechercheKeme(A, k):
    if A is None:
        return -1, k
    elif k == 1:
        return A.val, 0
    return rechercheKeme(A.ga, k-1)



# 7. Écrivez une procédure coupeSelon(A,x) qui, pour un ABR A et un élément x
#    (présent ou non dans A),retourne deux ABR:
#    un ABR contenant les éléments de A strictement inférieurs à x
#    et un ABR contenant les éléments de A strictement supérieurs à x.
#    Quels noeuds de A sont visités par la procédure coupeSelon(A,x)?


def coupeSelon(A, x):
    if A is not None:
        if x == A.val:
            return A.ga, A.dr
        elif x > A.val:
            cp_inf, cp_sup = coupeSelon(A.dr, x)
            A.dr = cp_inf
            return A, cp_sup
        elif x < A.val:
            cp_inf, cp_sup = coupeSelon(A.ga, x)
            A.ga = cp_sup
            return cp_inf, A



# test


# 8. Écrivez une procédure insereAlaRacine(A,x) qui retourne l'ABR A
#    où on ajoute l'élément x comme racine.
#    Vous utiliserez pour cela la procédure coupeSelon.
def insereALaRacine(A,x):
    inf, sup = coupeSelon(A, x)
    return Noeud(x, ga=inf, dr=sup)


# 9. Écrivez une procédure récursive fusion(A,B) qui retourne l'ABR
#    qui est la fusion des ABR A et B.
#    Vous utiliserez pour cela la procédure coupeSelon.
def fusion(A, B):
    if A is None:
        return B
    elif B is None:
        return A
    # TODO pas fini
    return


def tests():
    import copy
    unABR = Noeud(10, Noeud(5, None, Noeud(7)),
                  Noeud(13, Noeud(12, Noeud(11), None), Noeud(17)))
    unABR2 = Noeud(2,
                  Noeud(1,
                        None,
                        None),
                  Noeud(52,
                        Noeud(42,
                              Noeud(33),
                              None),
                        Noeud(420)))

    print(voir(unABR) + "\n")

    print(voir(minimum(copy.deepcopy(unABR))))

    print(voir(insere(copy.deepcopy(unABR), 2)))
    print("AFFICHAGE INTERVALLE 5 - 10")

    afficheIntervalle(copy.deepcopy(unABR), 5, 10)
    print("RECHERCHE 4 eme plus petite valeur")
    print(rechercheKeme(copy.deepcopy(unABR), 4))
    print("COUPE SELON 11")
    inf, sup = coupeSelon(copy.deepcopy(unABR), 11)
    print("INFERIEUR à 11")
    print(voir(inf))
    print("SUPERIEUR à 11")
    print(voir(sup))
    print("UNABR COMPLET")
    print(voir(unABR))
    print("INSERTION RACINE")
    print(voir(insereALaRacine(copy.deepcopy(unABR), 11)))
    print("FUSION ARBRES")
    print("ARBRE 1")
    print(voir(unABR))
    print("ARBRE 2")
    print(voir(unABR2))
    print("FUSION")
    print(voir(fusion(unABR, unABR2)))

tests()
