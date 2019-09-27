# read this: https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

#import pulp
#import os


class Problem:
    def __init__(self):
        self.name = ""
        self.type = "1"
        self.function = []
        self.constraints = []

    def function_to_string(self):
        string = ""
        
        if self.type == "1":
            string += "Max = "
        else:
            string += "Min = "
            
        if self.function:
            i = 1
            for variable in self.function:
                if variable >= 0:
                    string += "+ {}*X{} ".format(variable, i)
                else:
                    string += "- {}*X{} ".format(variable, i)
                i += 1
                
        return string

    def contraints_to_string(self):
        pass
        

problema = Problem()

def check_for_valid_input(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def input_variables():
    user = "this is something"

    print("Função objetivo")
    print("-------------------------------")
    print("Digite os coeficientes de cada")
    print("variável, uma de cada vez.")
    print("-------------------------------")
    print("Deixe o campo vazio para concluir!")

    i = 1

    while user != "":
        user = input("X{}: ".format(i))

        if user == "":
            if problema.function:
                print(problema.function_to_string())
            else:
                print("Nenhum valor salvo.")
                input("Aperte [ENTER] para retornar.")
                
        elif check_for_valid_input(user):
            problema.function.append(float(user))
            i += 1

        else:
            print("[ERRO] Input não válido como número!")

def input_constraints(problem:Problem):

    if not problem.function:
        print("[ERRO] Função vazia!")
        return

    size = len(problem.function)
    user = "this is something"

    print("Restrições da função")
    print("-------------------------------")
    print("Digite as sujeições à função objetivo,")
    print("uma variável por vez.")
    print("-------------------------------")
    print("Função objetiva:")
    print(problem.function_to_string())
    print("Deixe o campo vazio para cancelar/concluir!")

    i = 0
    restrictions = 0
    cancel = 0

    # Adding constraints for as long as there's input
    while user != "":
        print("{}º restrição:".format(restrictions+1))

        new_constraint = []
        j = size

        # For every variable there is
        while i < j:
            user = input("X{}: ".format(i+1))
            if check_for_valid_input(user):
                new_constraint.append(float(user))
                i += 1

            elif user == "":
                cancel = 1
                if i == 0:
                    print("Concluído!")
                    break
                else:
                    print("Cancelado!")
                    break
            else:
                print("[ERRO] Input não válido como número!")
        # <= a value

        while user != "":
            user = input("<= ")
            if check_for_valid_input:
                new_constraint.append(float(user))
                break

            elif user == "":
                print("Cancelado!")
                cancel = 1
                break

            else:
                print("[ERRO] Input não válido como número!")

        if not cancel:
            problem.constraints.append(new_constraint)
        i = 0
        restrictions += 1

def print_guided_problem_menu():
    """This function will guide the user into creating a new problem
    and allow them to add constraints that will then be passed to another function."""
    #os.system("cls")
    print("Criar novo problema")
    print("-------------------------------")
    print("Digite um nome para o problema")
    print("-------------------------------")
    print("Deixe o campo vazio para cancelar.")
    nome = input("Nome: ")

    if not nome:
        print("Nome vazio!")
        input("Aperte [ENTER] para retornar")
        return

    problema.name = nome

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
    
    problema.type = tipo

    input_variables()
    input_constraints(problema)
    
def print_main_menu():
    #os.system("cls")
    running = 1
    while running:
        print("Pesquisa Operacional")
        print("-------------------------------")
        print("1. Criar novo problema")
        print("2. Editar problema [not a feature]")
        print("3. Resolver problema [not a feature]")
        print("")
        print("8. Créditos")
        print("-------------------------------")
        print("0. Sair")
        print("")

        option = input("Opção: ")

        if option == "1":
            print_guided_problem_menu()

        elif option == "2":
            print("Feature is not ready.")
        else:
            running = 0

#os.system('mode con: cols=70 lines=20')
print_main_menu()
#input_variables()
#problema.function = [5.25, 4.5, 3.8, 10]
#input_constraints(problema)

"""
prob = pulp.LpProblem("How to maximize", pulp.LpMaximize)
x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)
prob += 2*x1 + 3*x2
prob += x1 + 5*x2 <= 20
prob += 2*x1 + x2 <= 10

result = prob.solve()
"""
