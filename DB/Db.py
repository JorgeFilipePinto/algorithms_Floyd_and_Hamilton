# Função responsável por imprimir as matrizes no nosso ficheiro TXT
def save(caminho, matrix1, matrix2):
    with open(caminho, 'a') as f:
        f.write("\n%30s" % "Matrix D:\n")
        for line in matrix1:
            f.write("%s\n" % line)
        if matrix2 != None:
            f.write("\n%30s" % "Matrix P:\n")
            for line in matrix2:
                f.write("%s\n" % line)

# Função responsável por imprimir separadores de valores no ficheiro TXT para uma melhor organização
def separador_save(caminho, text):
    with open(caminho, 'a') as f:
        f.write(40 * "-")
        f.write(text)
        f.write(40 * "-")
        f.write("\n")

# Função responsável por realizar o print das permutações no ficheiro TXT
def save_Hamilton(caminho, file):
    with open(caminho, 'a') as f:
        f.write("\n%30s" % "Combinações possiveis:\n")
        for line in file:
            f.write("%s\n" % str(line))


