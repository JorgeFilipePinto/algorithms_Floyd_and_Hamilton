from copy import deepcopy

inf = float("Inf")
Lista_D_Acores_ori = [[inf, 132, 155, 190, 283, 322],
                  [132, inf, 46, 69, 149, 192],
                  [155, 46, inf, 44, 262, 186],
                  [190, 69, 44, inf, 92, 145],
                  [283, 149, 262, 92, inf, 54],
                  [322, 192, 186, 145, 54, inf]]

mapa_acores = {"Lages": 0, "Horta": 1, "Praia": 2, "Angra": 3, "P.Delgada": 4, "V.do Porto": 5}

city_names = list(mapa_acores)                                                             # Transforma o dicionario em lista
for starting_city in city_names:                                                           # Percorre os elementos da lista
    custo_total = 0                                                                        # Inica a variavel
    Lista_D_Madeira = deepcopy(Lista_D_Acores_ori)                                         # Cria um clone da lista
    caminho_calculado = [starting_city]                                                    # Inicia a variavel do caminho calculado com o valor da Starting city
    idx_start = mapa_acores[starting_city]                                                 # Inicia a variavel com o valor da lista com o index da starting city
    custo_dos_vizinhos = Lista_D_Madeira[idx_start]                                        # Inicia a variavel com o valor da lista com index da idx start
    idx_do_vizinho_mais_proximo = custo_dos_vizinhos.index(min(custo_dos_vizinhos))        # Inicia a variavel com o indice do valor minimo da variavel de custo dos vizinhos

    for lista_de_custos in Lista_D_Madeira:
        lista_de_custos[idx_start] = inf                                                            # Passa a infinito a cidade em que já usei para iniciar o percurso

    while [x for x in custo_dos_vizinhos if x != inf]:                                              # Cria uma lista sem infinitos
        custo_total += custo_dos_vizinhos [idx_do_vizinho_mais_proximo]                             # Soma o valor obtido no index do vizinho mais proximo
        caminho_calculado.append(city_names[idx_do_vizinho_mais_proximo])                           # Acrescenta á lista caminho calculado a cidade com indx do vizinho mais proximo
        for lista_de_custos in Lista_D_Madeira:
            lista_de_custos[idx_do_vizinho_mais_proximo] = inf                                      # Passa a infinito a cidade em que já usei
        custo_dos_vizinhos = Lista_D_Madeira[idx_do_vizinho_mais_proximo]                    
        idx_do_vizinho_mais_proximo = custo_dos_vizinhos.index(min(custo_dos_vizinhos))             # Iguala a variavel com o indice do valor minimo da variavel de custo dos vizinhos

    custo_total += Lista_D_Acores_ori[idx_start][mapa_acores[caminho_calculado[-1]]]                # Para acrescentar o custo de voltar ao inicio (primeira cidade e a ultima)

caminho_calculado.sort()    
print(caminho_calculado)                                                                        # Faz print do caminho calculado
print(custo_total)                                                                              # Faz print do custo total do caminho