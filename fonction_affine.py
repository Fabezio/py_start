from math import floor as fl
from fractions import Fraction as ratio
from decimal import Decimal as dec

# fonction affine: déterminer coefficient directeur et ordonnée d'origine à partir de 2 paires de coordonnées (2 points) dans un repère orthonormé
x1 = int(input("abscisse 1: "))
y1 = int(input("ordonnée 1: "))
print(f"point1: ({x1}; {y1})")
x2 = int(input("abscisse 2: "))
y2 = int(input("ordonnée 2: "))
print(f"point2: ({x2}; {y2})")
a = 0
b = 0
def calcCoeff():
    if x2-x1 != 0:
        a = (y2-y1)/(x2-x1)
        #print (type(a))
        if a == fl(a):
            a = int(a)
        else: a = ratio(dec(a))
            
        print (f"a={a}")
        b = y2-a*x2
        if b == fl(b):
            b = int(b)
        #print (type(b))
        print (f"b={b}")
        # affichage final de l'équation
        """ 
        if a == 0:
            print(f"y={b}")
            
        if a == 1:

            if b > 0:
                print(f"y=x+{b}") 
            elif b < 0:
                print(f"y=x{b}") 
            elif b == 0:
                print(f"y=x") 
            # print(f"y={b}")

        if b > 0:
            print(f"y={a}x+{b}") 
        elif b < 0:
            print(f"y={a}x{b}") 
        elif b == 0:
            print(f"y={a}x")  """
        # graph = [x for x in range(-10, 10)]
        x3=int(input("nouvelle abscisse: "))
        y3=a*x3+b
        print(f"nouvelles valeurs: ({x3}; {y3})")

    else :
        print ("division par 0")





# print(f"a={calcCoeff()}")

# def calcOrigin():

# print(f"b={calcOrigin()}")
calcCoeff()