from itertools import permutations

def calc_Hamilton_circuits(cost_matrix, matrix_map):            # Recebe a matrix dos dados e o dicionbario mapa (nome e index)
    cities = list(matrix_map)                                   # Transforma o dicionario numa lista e guarda a na variavel cities
    cities_permutations = list(permutations(cities))            # Gera uma lista de permutações
    permutation_cost = []                                       # Inicia a lista de permutation_cost
    for permutation in cities_permutations:                     # O for irá percorrer dentro da lista de permutações
        permutation_val = 0
        for idx,city in enumerate(permutation):                 # O enumerate irá percorrerrer dentro do for anterior que por sua vez irá percorrer dentro da Lista de permutações e obterm o INDX e a City
            city1_matriz_idx = matrix_map[city]                 # Irá atribuir valor da index da lista matrix_map com o indice city
            city2_matriz_idx = matrix_map[permutation[(idx+1) % len(permutation)]]          # Impede que ultrapasse o tamanho da permutação
            permutation_val += cost_matrix[city1_matriz_idx][city2_matriz_idx]              # Soma á variavel o custo entre as coordenadas

        permutation_cost.append((permutation_val, permutation))                             # Adiciona á lista o valor e a permutação
    return permutation_cost                                                                 # Retorna a lista criada


