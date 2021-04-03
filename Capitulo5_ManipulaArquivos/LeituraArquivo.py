with open("teste.txt", "rb") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado variável ", type(conteudo))
print("Conteúdo do arquivo ", conteudo)