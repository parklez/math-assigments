# read this: https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

import pulp
#import os

#os.system('mode con: cols=70 lines=20')
def print_guided_problem_menu():
    """This function will guide the user into creating a new problem
    and allow them to add constraints that will then be passed to another function."""
    #os.system("cls")
    print("Criar novo problema")
    print("-------------------------------")
    print("Digite um nome para o problema")
    print("Deixe o campo vazio para cancelar.")
    print("-------------------------------")
    nome = input("Nome: ")

    if not nome:
        print("Nome vazio!")
        input("Aperte [ENTER] para retornar")
        return

    print("Tipo de problema")
    print("-------------------------------")
    print("1. Maximizar")
    print("2. Minimizar")
    print("-------------------------------")
    tipo = input("Número: ")

    if tipo not in ("1", "2"):
        print("[ERRO] Opção inválida, operação cancelada!")
        input("Aperte [ENTER] para retornar")
        return
    

def print_main_menu():
    #os.system("cls")
    running = 1
    while running:
        print("Pesquisa Operacional")
        print("-------------------------------")
        print("1. Criar novo problema")
        print("2. Editar problema")
        print("3. Resolver problema")
        print("")
        print("8. Créditos")
        print("-------------------------------")
        print("0. Sair")
        print("")

        option = input("Opção: ")

        if option == "1":
            print_guided_problem_menu()

        else:
            running = 0

print_main_menu()

"""
prob = pulp.LpProblem("How to maximize", pulp.LpMaximize)
x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)
prob += 2*x1 + 3*x2
prob += x1 + 5*x2 <= 20
prob += 2*x1 + x2 <= 10

result = prob.solve()
"""
