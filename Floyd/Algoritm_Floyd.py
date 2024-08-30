

def algoritmo_floyd(Lista_Entrada, Lista_Vertices):
    inf = float("Inf") # Variavel para identificar
    
    for i in range(len(Lista_Entrada)): 
        for j in range(len(Lista_Entrada)): 
            if Lista_Entrada[i][j]<inf:
                Lista_Vertices[i][j] = i+1
                
# Nesta instância irá correr um ciclo for dentro de outro em que ambos têm uma range que irá ser do tamanho da lista que a função irá receber. 
# De seguida o ciclo irá correr as duas matrizes de entrada em que o i será responsável por navegar nas linhas das nossas matrizes e o j por 
# navegar dentro das colunas de cada linha, ou seja, vai correr os nossos elementos. Enquanto realiza essa operação existe uma condição que caso
# a matriz dos dados (matriz entrada) obtenha um valor inferior a inf (infinito) a matriz dos vértices na mesma instância de i, j coloca o seu 
# valor a i+1 (+1 para evitar zeros pois a mesma foi iniciada com os mesmos), isto vai nos dar as coordenadas dos nossos vértices e onde os mesmos 
# estão ligados pois i é referente á nossa linha

    for k in range(len(Lista_Entrada)):
        for i in range(len(Lista_Entrada)):
            for j in range (len(Lista_Entrada)):
                if Lista_Entrada[i][k] + Lista_Entrada[k][j] < Lista_Entrada[i][j]:
                    Lista_Entrada[i][j] = Lista_Entrada[i][k] + Lista_Entrada[k][j]
                    Lista_Vertices[i][j] = Lista_Vertices[k][j]

    return Lista_Entrada, Lista_Vertices

# O algoritmo irá correr dentro de 3 ciclos for em que os mesmos são responsáveis por:
# Ciclo K (criação das matrizes dos diversos estágios do algoritmo ou seja irá criar tantas matrizes como o tamanho da matriz de entrada).
# Ciclo i (responsável por fazer a varrimento das nossas linhas da matriz).
# Ciclo j(responsável por fazer o varrimento das colunas da linha da matriz, ou seja, os elementos).

# Enquanto ocorre os varrimentos de todos os elementos da matriz existe uma condição que se a soma do 
# elemento da matriz na instância (i, k) com (k, j) for inferior ao elemento da matriz na instancia (i, j) 
# irá alterar o valor na instancia (i, j) para o valor da respetiva soma. Alterando assim de seguida também a 
# matriz dos vértices em que ira alterar o valor em (i, j) pelo valor da mesma em (k, j).