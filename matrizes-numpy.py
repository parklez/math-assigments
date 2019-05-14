#!usr/bin/python3

"""
Este código realiza operações com duas matrizes.
github.com/parklez
"""
import numpy as np
import sys


print(__doc__)

print("Qual operação deseja realizar?")
print("-------------------------------")
print("0 - Multiplicação")
print("1 - Subtração")
print("2 - Adição")
print("3 - Inversão")
print("-------------------------------")

op = int(input("Número: "))

print("\nDigite as matrizes no formato LxC,\nOnde L e C são numeros inteiros representando\na quantidade de linhas e colunas respectivamente.\nExemplo: 1x2")
da = input("Digite a dimensão da matriz A: ")
if op != 3:
    db = input("Digite a dimensão da matriz B: ")
print("")

la = int(da.split("x")[0])
ca = int(da.split("x")[1])
if op != 3:
    lb = int(db.split("x")[0])
    cb = int(db.split("x")[1])

# Verificar se a operação é possível

def fim():
    input("Aperte ENTER para fechar a janela.")
    sys.exit()

if la == 0 or ca == 0:
    print("Impossível realizar operações com alguma dimensão 0.")
    fim()

if op != 3:
    if lb == 0 or cb == 0:
        print("Impossível realizar operações com alguma dimensão 0.")
        fim()
    
if op == 0:
    if ca != lb:
        print("Erro! Dimensão de coluna da Matriz A {},{} não é igual a dimensão de linha da Matriz B {},{}.".format(la,ca,lb,cb))
        fim()

if op == 1 or op == 2:
    if da != db:
        print("Erro! Não se pode somar ou subtrair matrizes de dimensões diferentes!")
        fim()

array_a = []
array_b = []

for line in range(1, la+1):
    temp_line = []
    for column in range(1, ca+1):
        string = ""
        number = int(input("Matriz A, número de posição {},{}: ".format(line, column)))
        temp_line.append(number)
    array_a.append(temp_line)

print("")

if op != 3:
    for line in range(1, lb+1):
        temp_line = []
        for column in range(1, cb+1):
            string = ""
            number = int(input("Matriz B, número de posição {},{}: ".format(line, column)))
            temp_line.append(number)
        array_b.append(temp_line)

a = np.matrix(array_a)
b = np.matrix(array_b)

if op == 0:
    c = a * b

elif op == 1:
    c = a - b
    
elif op == 2:
    c = a + b

elif op == 3:
    try:
        c = a.getI()
    except Exception as e:
        print("Não foi possível calcular matriz inversa!", e)
        fim()

print("")
print("Matriz A:")
print(a)

if op != 3:
    print("Matriz B:")
    print(b)
    
print("Matriz Resultante:")
print(c)

print("")
fim()
