# Importação dos nossos módulos
from Floyd.Algoritm_Floyd import algoritmo_floyd
from Matrix.Matrix import matrix_separador_matrix, matrix_list_print_with_city, matrix_diagonal_line_matrix, matrix_print
from DB.Db import save,separador_save
from Menu.menu import menu_city, menu_choice, menu_final_print

inf = float("Inf")
M_Dados = [[0,2,inf,inf,1],                                             # Matrix dos nossos dados, neste caso distâncias entre os vértices
           [2,0,1,4,8], 
           [inf,1,0,2,inf], 
           [inf, 4, 2, 0, 10], 
           [1, 8, inf, 10, 0]]

M_V = [[0, 0, 0, 0, 0],                                                 # Matrix dos vertices
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0],]

vertice_list = ["1", "2", "3", "4", "5"]                                # Lista para identificação dos nomes dos nossos vértices

matrix_separador_matrix("Matrizes Iniciais")                            # Envia a string para a função matrix separador
separador_save('Files_TXT\Floyd_1.txt', "Matrizes Iniciais")            # Envia a string para a função que irá criar um separador no ficheiro TXT
save('Files_TXT\Floyd_1.txt', M_Dados, M_V)
matrix_separador_matrix("Matrix Dados")                                 # Envia a string para a função matrix separador
matrix_print(M_Dados, vertice_list)                                     # Envia a matrix e realiza o print da mesma
matrix_separador_matrix("Matrix dos Vertices")                         # Envia a string para a função matrix separador
matrix_print(M_V, vertice_list)                                                       # Envia a matrix e realiza o print da mesma

matrix_separador_matrix("Inicio do Algoritmo")                        # Envia a string para a função matrix separador
algoritmo_floyd(M_Dados, M_V)                                         # Envia as matrizes para a função iniciar o algoritmo
matrix_separador_matrix("Matrix Dados")                               # Envia a string para a função matrix separador
matrix_print(M_Dados, vertice_list)                                   # Envia a matrix e realiza o print da mesma
matrix_separador_matrix("Matrix dos Vertices")                        # Envia a string para a função matrix separador
matrix_print(M_V, vertice_list)                                                     # Envia a matrix e realiza o print da mesma

separador_save('Files_TXT\Floyd_1.txt', "Matrizes Finais")            # Envia a string para a função que irá criar um separador no ficheiro TXT
save('Files_TXT\Floyd_1.txt', M_Dados, M_V)                            # Envia as matrizes para a função iniciar o print das mesmas no ficheiro TXT
matrix_separador_matrix("Matrix Dados")                               # Envia a string para a função matrix separador
matrix_print(M_Dados, vertice_list)                                   # Envia a matrix e realiza o print da mesma
matrix_separador_matrix("Matrix dos Vertices")                       # Envia a string para a função matrix separador
matrix_print(M_V, vertice_list)                                                    # Envia a matrix e realiza o print da mesma

matrix_diagonal_line_matrix(M_Dados)                               # Envia as matrizes para a função iniciar a eliminação dos elementos da diagonal
separador_save('Files_TXT\Floyd_1.txt', "Diagonal Eliminada")        # Envia a string para a função que irá criar um separador no ficheiro TXT
save('Files_TXT\Floyd_1.txt', M_Dados, M_V)                           # Envia as matrizes para a função iniciar o print das mesmas no ficheiro TXT

matrix_separador_matrix("Matrix Dados")                               # Envia a string para a função matrix separador
matrix_print(M_Dados, vertice_list)                                    # Envia a matrix e realiza o print da mesma
matrix_separador_matrix("Matrix dos Vertices")                         # Envia a string para a função matrix separador
matrix_print(M_V, vertice_list)                                                      # Envia a matrix e realiza o print da mesma

menu_city(vertice_list, "o vertice")                                                # Envia a lista dos nomes dos vértices para a função apresentar ao utilizador para escolher o caminho desejado

vertice1 = int(input("Escolha o seu primeiro vértice!!\n"))            # Input de utilizador para a escolha o primeiro vertice e armazenar o index em vertice1
vertice2 = int(input("Escolha o seu segundo vértice!!\n"))            # Input de utilizador para a escolha o segundo vertice e armazenar o index em vertice2


menu_choice("Os Vertices", vertice_list, vertice1, vertice2)                                  # Envia os elementos (lista de vertices, index 1 e index 2) para a função

 # Envia os elementos (lista de vertices, matrix dos dados, matrix dos vertices, index 1 e index 2, texto das unidades entre vertices, tipologia dos vertices) para a função
menu_final_print("O Vertice", vertice_list, M_Dados, M_V, vertice1, vertice2, "valores")            
