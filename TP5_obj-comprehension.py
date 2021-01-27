# squared = [i**2 for i in range (20)]
sqDico = {k:v for k, v in enumerate([i**2 for i in range (20+1)])}
print(sqDico)