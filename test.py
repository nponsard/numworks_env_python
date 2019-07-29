from math import *


print("initialisé")


def racine(a, b, c):
    delta = b**2-4*a*c
    if delta > 0:
        print("deux solutions :")
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        print(x1, x2)
    elif delta == 0:
        print("une solution :")
        print(-b/(2*a))
    else:
        print("il n'y a pas de solution réelle")
