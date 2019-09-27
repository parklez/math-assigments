#import pulp
#https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html
import os


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
                    string += "- {}*X{} ".format(variable *-1, i)
                i += 1
                
        return string

    def constraints_to_string(self):
        string = ""
        for constraint in self.constraints:
            line = ""
            size = len(constraint)
            i = 1
            for variable in constraint:
                # If this is the last variable.... <=
                if i == size:
                    line += "<= {}".format(variable)
                else:
                    if variable >= 0:
                        line += "+ {}*X{} ".format(variable, i)
                    else:
                        line += "- {}*X{} ".format(variable *-1, i)
                    i += 1

            string += line + '\n'
            
        i = 1
        for variable in self.function:
            string += "X{}, ".format(i)
            i += 1

        string = string[:-2]
        string += " >= 0"

        return string

problema = Problem()

def check_for_valid_input(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def input_variables(problem:Problem):
    os.system("clear")

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
            if problem.function:
                print("Função objetiva:")
                print(problem.function_to_string())
                input("Aperte [ENTER] para continuar.")

            else:
                print("Nenhum valor salvo.")
                input("Aperte [ENTER] para retornar.")
                
        elif check_for_valid_input(user):
            problem.function.append(float(user))
            i += 1

        else:
            print("[ERRO] Input não válido como número!")

def input_constraints(problem:Problem):
    os.system("clear")

    if not problem.function:
        print("[ERRO] Função vazia!")
        return

    size = len(problem.function)
    user = "this is something"

    print("Restrições da função")
    print("-------------------------------")
    print("Digite as sujeições à função objetiva,")
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

def print_guided_problem_menu(problem:Problem):
    """This function will guide the user into creating a new problem
    and allow them to add constraints that will then be passed to another function."""

    if problem.function:
        os.system("clear")
        print("Já existe uma função objetiva,")
        print("deseja criar uma nova?")
        print("-------------------------------")
        print("1. Sim")
        print("2. Não")
        print("-------------------------------")
        user = input("Opção: ")

        if user == "1":
            problem.constraints = []
            problem.function = []
        
        # this is painful
        else:
            print("Operação cancelada.")
            input("Aperte [ENTER] para retornar.")
            return

    os.system("clear")
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

    problem.name = nome
    os.system("clear")
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
    
    problem.type = tipo

    input_variables(problem)
    input_constraints(problem)

def print_modelo_padrao(problem:Problem):
    os.system("clear")

    if not problem.function:
        print("Não há função objetiva.")
        input("Aperte [ENTER] para retornar.")
        return

    print("Modelo padrão")
    print("-------------------------------")
    print("Função objetiva:")
    print(problem.function_to_string())
    print("")
    print("Sujeita às condições:")
    print(problem.constraints_to_string())
    print("-------------------------------")
    input("Aperte [ENTER] para retornar ao menu principal.")

def remove_constraint_menu(problem:Problem):
    os.system("clear")
    if not problem.constraints:
        print("Não há restrições para remover.")
        input("Aperte [ENTER] para retornar.")
        return

    i = 0
    clist = problem.constraints_to_string().split("\n")[:-1]

    print("Remover restrição")
    print("-------------------------------")
    for constraint in clist:
        print("{}. {}".format(i, constraint))
        i += 1
    print("-------------------------------")
    print("Deixa o campo vazio para cancelar.")
    user = input("Opção: ")

    if user == "":
        print("Nenhuma alteração feita.")
        input("Aperte [ENTER] para retornar.")
        return

    try:
        problem.constraints.pop(int(user))
        print("Restrição removida com sucesso!")
        input("Aperte [ENTER] para retornar.")
    except:
        print("[ERRO] Input não válido!")
        input("Aperte [ENTER] para retornar.")
    return

def edit_constraints(problem:Problem):
    
    running = 1
    while running:
        os.system("clear")
        print("Editar restrições")
        print("-------------------------------")
        print("1. Remover existentes")
        print("2. Adicionar restrição")
        print("-------------------------------")
        print("0. Retornar")
        user = input("Opção: ")

        if user == "1":
            remove_constraint_menu(problem)

        elif user == "2":
            input_constraints(problem)
        
        elif user == "0":
            return

        else:
            print("[ERRO] Opção não válida.")
            input("Aperte [ENTER] para continuar.")

def edit_function(problem:Problem):
    os.system("clear")
    i = 0

    print("Editar função objetiva")
    print("-------------------------------")
    print("Função atual:")
    print(problem.function_to_string())
    print("")
    print("Digite novos valores para cada variável.")
    print("-------------------------------")
    print("Deixe o campo vazio para cancelar.")

    new_function = list()
    size = len(problem.function)
    while i < size:
        new = input("X{}: ".format(i+1))
        if new == "":
            print("Operação cancelada.")
            input("Aperte [ENTER] para retornar.")
            return

        elif check_for_valid_input(new):
            new_function.append(float(new))
            i += 1
        else:
            print("[ERRO] Input não válido como número!")
            input("Aperte [ENTER] para continuar.")


    problem.function = list(new_function)
    print("Nova função salva com sucesso.")
    input("Aperte [ENTER] para retornar.")

def edit_problem(problem:Problem):
    os.system("clear")

    if not problem.function:
        print("[ERRO] Não existe função objetiva.")
        input("Aperte [ENTER] para retornar.")
        return

    running = 1
    while running:
        os.system("clear")
        print("Editar problema")
        print("-------------------------------")
        print("1. Editar função")    
        print("2. Editar restrições")
        print("-------------------------------")
        print("0. Retornar")
        option = input("Opção: ")

        if option == "1":
            edit_function(problem)

        elif option == "2":
            edit_constraints(problem)
            pass
        
        elif option == "0":
            return

def print_copyright():
    os.system("clear")
    print("Copyright")
    print("-------------------------------")
    print("parklez @ github.com/parklez")
    print("-------------------------------")
    input("Press [ENTER] to return...")

def print_main_menu():
    running = 1
    while running:
        os.system("clear")
        print("Pesquisa Operacional")
        print("-------------------------------")
        print("1. Criar novo problema")
        print("2. Editar problema")
        print("3. Visualizar modelo padrão")
        print("4. Resolver problema [not a feature]")
        print("")
        print("9. Créditos")
        print("-------------------------------")
        print("0. Sair")
        print("")

        option = input("Opção: ")

        if option == "1":
            print_guided_problem_menu(problema)

        elif option == "2":
            edit_problem(problema)

        elif option == "3":
            print_modelo_padrao(problema)

        elif option == "9":
            print_copyright()

        elif option == "0":
            running = 0

#os.system('mode con: cols=70 lines=20')
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
