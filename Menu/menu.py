
# Função responsável pela impressão do nosso menu através de um ciclo for imprimimos o index da nossa lista juntamente com o seu elemento juntanto entre eles uma seta "->"
def menu_city (list, elemento):
    print("Escolha", elemento, ":")
    for idx in range(len(list)):
        print(f" {idx} -> {list[idx]}\n")

# Função responsável por imprimir as escolhas que o utilizador optou
def menu_choice(elment, matrix, v1, v2):
    print(elment, "que escolheu são", matrix[v1], "para", matrix[v2],".\n") # Faz print das cidades escolhidas

# Função responsável por apresentar o valor final
def menu_final_print(elment, list, matrix1, matrix2, v1, v2, text1):
      print( elment, list[v1], "fica a ", matrix1[v1][v2], text1,"de", list[v2], ".")

def menu_hamilton():
     print("Qual das ilhas pretende descobrir o melhor circuito de Hamilton?\n")
     print("0 -> Açores\n")
     print("1 -> Madeira\n")