# Função responsável por realizar o print da matrix que o utilizador inserir
def matrix_print(matrix, name):
    for indx in range(len(matrix)):
        print("%15s" % name[indx], matrix[indx])
    print("\n")

# Função responsável por realizar um print de tracejado e no meio do mesmo o texto que o utilizador inserir na função
def matrix_separador_matrix(Text):
    print(90 * "-", Text, 90 * "-", "\n")

# Função para eliminar os elementos que se encontram na diagonal da matrix pois os mesmos não são necessários, pois a distância entre a mesma cidade é zero
def matrix_diagonal_line_matrix(matrix1):
    for line in range(len(matrix1)):
        for colunn in range(len(matrix1)):
            if line == colunn:
                matrix1[line][colunn] = 0
            else:
                continue

# Função com ciclo for para apresentação da nossa matrix mais percetivel
def matrix_list_print_with_city(matrix1, matrix2, name):
    print("%50s" % "Matrix dos Vertice:", "%80s" % "Matrix dos Dados:\n")
    for indx in range(len(matrix1)):
        print("%15s" % name[indx], matrix2[indx], "%15s" % name[indx], matrix1[indx], "\n")