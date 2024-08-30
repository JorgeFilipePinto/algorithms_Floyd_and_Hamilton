inf = float("Inf")
from copy import deepcopy

Lista_D_Madeira_ori = [[inf, 41, 35, 179, 183],
                  [41, inf, 22, 162, 165],
                  [35, 22, inf, 149, 154],
                  [179, 162, 149, inf, 11],
                  [183, 165, 154, 11, inf]]

mapa_Madeira = {"P. Santo": 0, "Funchal": 1, "Desertas": 2, "Selvagem Gr.": 3, "Selvagem Pq.": 4}

city_names = list(mapa_Madeira)                                                             # Transforma o dicionario em lista
for starting_city in city_names:                                                            # Percorre os elementos da lista
    custo_total = 0                                                                         # Inica a variavel
    Lista_D_Madeira = deepcopy(Lista_D_Madeira_ori)                                         # Cria um clone da lista
    caminho_calculado = [starting_city]                                                     # Inicia a variavel do caminho calculado com o valor da Starting city
    idx_start = mapa_Madeira[starting_city]                                                 # Inicia a variavel com o valor da lista com o index da starting city
    custo_dos_vizinhos = Lista_D_Madeira[idx_start]                                         # Inicia a variavel com o valor da lista com index da idx start
    idx_do_vizinho_mais_proximo = custo_dos_vizinhos.index(min(custo_dos_vizinhos))         # Inicia a variavel com o indice do valor minimo da variavel de custo dos vizinhos

    for lista_de_custos in Lista_D_Madeira:
        lista_de_custos[idx_start] = inf                                                    # Passa a infinito a cidade em que já usei para iniciar o percurso

    while [x for x in custo_dos_vizinhos if x != inf]:                                      # Cria uma lista sem infinitos
        custo_total += custo_dos_vizinhos [idx_do_vizinho_mais_proximo]                     # Soma o valor obtido no index do vizinho mais proximo
        caminho_calculado.append(city_names[idx_do_vizinho_mais_proximo])                   # Acrescenta á lista caminho calculado a cidade com indx do vizinho mais proximo
        for lista_de_custos in Lista_D_Madeira:
            lista_de_custos[idx_do_vizinho_mais_proximo] = inf                              # Passa a infinito a cidade em que já usei
        custo_dos_vizinhos = Lista_D_Madeira[idx_do_vizinho_mais_proximo]                    
        idx_do_vizinho_mais_proximo = custo_dos_vizinhos.index(min(custo_dos_vizinhos))     # Iguala a variavel com o indice do valor minimo da variavel de custo dos vizinhos

    custo_total += Lista_D_Madeira_ori[idx_start][mapa_Madeira[caminho_calculado[-1]]]       # Para acrescentar o custo de voltar ao inicio (primeira cidade e a ultima)

caminho_calculado.sort()
print(caminho_calculado)                                                                 # Faz print do caminho calculado
print(custo_total)                                                                       # Faz print do custo total do caminho
