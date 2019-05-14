"""
--------------------------------------------------------------------------------
  _____                               /\/|         _ _                       
 |  __ \                             |/\/         | (_)                      
 | |__) |___  __ _ _ __ ___  ___ ___  __ _  ___   | |_ _ __   ___  __ _ _ __ 
 |  _  // _ \/ _` | '__/ _ \/ __/ __|/ _` |/ _ \  | | | '_ \ / _ \/ _` | '__|
 | | \ \  __/ (_| | | |  __/\__ \__ \ (_| | (_) | | | | | | |  __/ (_| | |   
 |_|  \_\___|\__, |_|  \___||___/___/\__,_|\___/  |_|_|_| |_|\___|\__,_|_|   
              __/ |                                                          
             |___/                                                           
--------------------------------------------------------------------------------
source code @ github.com/parklez
"""
import os
import math


def main():
    os.system('cls')
    
    print("----------------")
    print("Entrada de dados")
    print("----------------")
    
    xy = []

    n = int(input("> Digite a quantidade N de elementos a ser trabalhado: "))
    print("> Agora digite os valores de X e Y para cada par.")
    print('-----')
    
    for pair in range(0, n):
        x = int(input("{}° X: ".format(pair+1)))
        y = int(input("{}° Y: ".format(pair+1)))
        xy.append([x, y])
        print('-----')
    
    xi = 0
    xi_squared = 0
    yi = 0
    yi_squared = 0
    xiyi = 0
    
    for pair in range(0, n):
        xi += xy[pair][0]
        xi_squared += xy[pair][0]**2
        yi += xy[pair][1]
        yi_squared += xy[pair][1]**2
        xiyi += xy[pair][0] * xy[pair][1]
    
    print("")
    print("Total = xi: {} yi: {} xi^2: {} yi^2: {} xiyi: {}".format(xi, yi, xi_squared, yi_squared, xiyi))
    
    r = ((n * xiyi) - (xi * yi)) / math.sqrt((((n * xi_squared) - (xi**2)) * ((n * yi_squared) - (yi ** 2))))
    
    print("--------------------------")
    print("Coeficiente de correlação:")
    print("--------------------------")
    print("")
    print("                 {} x {} - {} x {}".format(n, xiyi, xi, yi))
    print("r = ----------------------------------------------  = {} = {:.2%}".format(r, r))
    print("      √([{} x {} - {}²] x [{} x {} - {}²])".format(n, xi_squared, xi, n, yi_squared, yi))    
    
    b = ((n * xiyi) - (xi*yi)) / ((n * xi_squared) - (xi ** 2))
    
    print("")
    print("---------------------------")
    print("Modelagem - Equação da reta")
    print("---------------------------")
    print("")
    print("        {} x {} - {} x {}".format(n, xiyi, xi, yi))
    print("b = --------------------------- = {}".format(b))
    print("         {} x {} - {}²".format(n, xi, xi))
    
    a = (yi / n) - (b * (xi/n))
    
    print("")
    print("a = {}/{} - {}*{}/{} = {}".format(yi, n, b, x, n, a))
    print("")
    print("y = bx + a")
    print("y = {:.5}x + {:.5}".format(b, a))
    
    print("")
    print("------------------------------")
    print("Deseja realizar outro calculo?")
    print("------------------------------")
    print("1. Sim")
    print("2. Não")
    answer = input("Número:")
    if answer == "1":
        main()
    else:
        return

if __name__ == "__main__":
    print(__doc__)
    input("Aperte [ENTER] para começar...")
    
    main()
