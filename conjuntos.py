#!usr/bin/python3

"""
Este código calcula a união de conjuntos.
github.com/parklez
"""
from math import factorial as fac


print(__doc__)
conjuntos = int(input("Insira a quantidade de conjuntos a ser trabalhado: "))
print("Digite a quantidade de pessoas formadas nas sequintes condições:")

array = []

i = 1
u = 1

for conjunto in range(0, conjuntos):
    c = fac(conjuntos)/(fac(i)*fac(conjuntos-i))
    c = int(c)
    temp = []
        temp.append(n)
        u += 1
    i += 1
    u = 1
    array.append(temp)

# União
i = 0
uniao = 0
formula = "Formula: "
for conjunto in array:
    if i == 0:
        uniao += sum(conjunto)
        formula += str(conjunto) + " - " 
        i = 1
    else:
        uniao -= sum(conjunto)
        formula += str(conjunto) + " + " 
        i = 0

formula = formula[:-3]

print("\n" + formula + "\n")
print("A união dos elementos formados por {0} grupos é igual a {1} pessoas.".format(conjuntos, uniao))
input("")
