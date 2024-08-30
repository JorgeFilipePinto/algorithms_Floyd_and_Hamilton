# Importação dos nosso módulos
from Floyd.Algoritm_Floyd import algoritmo_floyd
from Matrix.Matrix import matrix_separador_matrix, matrix_list_print_with_city, matrix_diagonal_line_matrix
from DB.Db import save,separador_save
from Menu.menu import menu_city, menu_choice, menu_final_print

inf = float("Inf") # Variavel para identificar
# Matrix com os valores do nosso grafo
Data_Base = [
            [inf, 50, inf, inf, 80, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
            [50, inf, inf, 100, 50, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, 140, inf, inf, inf, 200, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, 100, 140, inf, 120, inf, 110, 150, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [80, 50, inf, 120, inf, 70, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, inf, 70, inf, 100, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, 110, inf, 100, inf, 80, 80, inf, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, 200, 150, inf, inf, 80, inf, 160, 100, inf, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, inf, inf, 80, 80, 160, inf, 160, 70, inf, inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, inf, inf, inf, inf, 100, 160, inf, inf, 200, 80, inf, inf, inf, inf, inf],
            [inf, inf, inf, inf, inf, inf, inf, inf, 70, inf, inf, inf, inf, 130, inf, inf, inf, inf],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, 200, inf, inf, 150, 70, 120, inf, inf, inf],      
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, 80, inf, 150, inf, inf, 100, inf, inf, inf],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 130, 70, inf, inf, 150, 50, inf, inf],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 120, 100, 150, inf, inf, 80, inf],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 50, inf, inf, 135, 260],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 80, 135, inf, 170],
            [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 260, 170, inf]
           ]

# Matrix iniciação para apresentação do valor de nº de vértices, a maesma quando pronta irá apresentar o valor do número de vercices necessarios entre as cidades
Lista_P = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# Lista para indexação dos vertices e a relação dos nomes aos vértices
city_list = ["Viana do Castelo", "Braga", "Bragança", "Vila Real", "Porto", "Aveiro", "Viseu",
             "Guarda", "Coimbra", "Castelo Branco", "Leiria", "Santarém", "Portalegre",
             "Lisboa", "Évora", "Setubal", "Beja", "Faro"]

# Envias as Strings para as funções 
matrix_separador_matrix("Matrizes Iniciais")
separador_save('Files_TXT\Floyd_2.txt', "Matrizes Iniciais")

# Envia os elementos para a função
save('Files_TXT\Floyd_2.txt', Data_Base, Lista_P)
matrix_list_print_with_city(Data_Base, Lista_P, city_list)

# Envia os elementos para a função e para o algoritmo
matrix_separador_matrix("Inicio do Algoritmo")
algoritmo_floyd(Data_Base, Lista_P)
matrix_list_print_with_city(Data_Base, Lista_P, city_list)

# Envia os elementos para a função
separador_save('Files_TXT\Floyd_2.txt', "Matrizes Finais")
save('Files_TXT\Floyd_2.txt', Data_Base, Lista_P)

matrix_separador_matrix("Diagonal eliminada")
matrix_diagonal_line_matrix(Data_Base)
matrix_list_print_with_city(Data_Base, Lista_P, city_list)
# Envia a nossa matrix de dados, a matrix P e a lista com as cidades para a nossa função
separador_save('Files_TXT\Floyd_2.txt', "Diagonal eliminada")
save('Files_TXT\Floyd_2.txt', Data_Base, Lista_P)

# Envia a nossa lista para a função
menu_city(city_list, "a cidade")

city1 = int(input("Escolha a sua primeira cidade!!\n")) # Input de utilizador para a escolha da primeira cidade e armazenar o index da mesma em city1
city2 = int(input("Escolha a sua segunda cidade!!\n"))  # Input de utilizador para a escolha da segunda cidade e armazenar o index da mesma em city2

# Envia os elementos para a função
menu_choice("As cidades", city_list, city1, city2)

# Envia os elementos para a função
menu_final_print("A cidade", city_list, Data_Base, Lista_P, city1, city2, "kilometros")