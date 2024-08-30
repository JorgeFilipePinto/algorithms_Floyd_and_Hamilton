# Importação dos nossos módulos
from itertools import permutations
from Hamilton.Algoritm_hamilton import calc_Hamilton_circuits
from DB.Db import save_Hamilton, separador_save, save
from Menu.menu import menu_hamilton

inf = float("Inf")
Lista_D_Acores = [[inf, 132, 155, 190, 283, 322],[132, inf, 46, 69, 149, 192],[155, 46, inf, 44, 262, 186],
                  [190, 69, 44, inf, 92, 145],[283, 149, 262, 92, inf, 54],[322, 192, 186, 145, 54, inf]]
mapa_acores = {"Lages": 0, "Horta":1, "Praia": 2, "Angra": 3, "P.Delgada": 4, "V.do Porto": 5}

Lista_D_Madeira = [[inf, 41, 35, 179, 183],[41, inf, 22, 162, 165],[35, 22, inf, 149, 154],
                   [179, 162, 149, inf, 11],[183, 165, 154, 11, inf]]
mapa_madeira ={"P. Santo": 0, "Funchal": 1, "Desertas": 2, "Selvagem Gr.": 3, "Selvagem Pq.":4}

menu_hamilton()
escolha_ilha = int(input("Escolha!\n"))
if escolha_ilha == 0:
    print("Escolheu calcular o circuito de Hamilton do Açores.\n")

    permutation_cost = calc_Hamilton_circuits(Lista_D_Acores, mapa_acores)                       # Irá resultar no número facturial de hipotese neste caso as 720
    min_cost, min_circuit = min(permutation_cost)                                                # Irá automaticamente escolher o caminho mais curto das 720 hipoteses
    permutation_cost.sort()                                                                      # Coloca a nossa permutação por ordem para assim ter uma leitura mais facilitada
    
    # Imprime o valor de quantas permutações existem
    print("Existem", len(calc_Hamilton_circuits(Lista_D_Acores, mapa_acores)), "hipotes possíveis.\n")
    # Imprime o valor da permutação
    print("Circuito de Hamilton", min(permutation_cost), "\n")
    # Imprime o circuito e o valor total
    print(f"O melhor circuito de Hamilton dos Açores é de {' -> '.join(min_circuit)} e tem um comprimento de aproximadamente {int(min_cost * 1.8)} kilometros\n")
    
    separador_save("Files_TXT\Hamilton_Acores.txt", "Matrix dos Açores")                        # Imprime no ficheiro TXT um separador com o texto enviado para a função
    save("Files_TXT\Hamilton_Acores.txt", Lista_D_Acores, None)                                 # Imprime no ficheiro TXT a matrix enviada para a função
    save_Hamilton("Files_TXT\Hamilton_Acores.txt", permutation_cost)                            # Imprime no ficheiro TXT a permutação
elif escolha_ilha == 1:
    print("Escolheu calcular o circuito de Hamilton da Madeira.\n")
    
    permutation_cost = calc_Hamilton_circuits(Lista_D_Madeira, mapa_madeira)                     # Irá resultar no número facturial de hipotese neste caso as 720
    min_cost, min_circuit = min(permutation_cost)                                                # Irá automaticamente escolher o caminho mais curto das 720 hipoteses
    permutation_cost.sort()                                                                      # Coloca a nossa permutação por ordem para assim ter uma leitura mais facilitada
    
    # Imprime o valor de quantas permutações existem
    print("Existem", len(calc_Hamilton_circuits(Lista_D_Madeira, mapa_madeira)), "hipotes possíveis.\n")
    # Imprime o valor da permutação
    print("Circuito de Hamilton", min(permutation_cost), "\n")
    # Imprime o circuito e o valor total
    print(f"O melhor circuito de Hamilton da Madeira é de {' -> '.join(min_circuit)} e tem um comprimento de aproximadamente {int(min_cost * 1.8)} kilometros\n")

    separador_save("Files_TXT\Hamilton_Madeira.txt", "Matrix dos Açores")                           # Imprime no ficheiro TXT um separador com o texto enviado para a função
    save("Files_TXT\Hamilton_Madeira.txt", Lista_D_Madeira, None)                                   # Imprime no ficheiro TXT a matrix enviada para a função
    save_Hamilton("Files_TXT\Hamilton_Madeira.txt", permutation_cost)                               # Imprime no ficheiro TXT a permutação
else:
    print("A opção pretendida não é válida!")