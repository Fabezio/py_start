print('classeur')
classeur = {"positifs": [], "negatifs": []}
print(classeur)
nombres= [-2, 0, -3, 5, 8]
print(nombres)

for  nb in nombres:
    print(nb)
    if nb >= 0:
            classeur["positifs"].append(nb)
    if nb <= 0:
            classeur["negatifs"].append(nb)

for sign, num in classeur.items():
    print (sign+ ":", num)