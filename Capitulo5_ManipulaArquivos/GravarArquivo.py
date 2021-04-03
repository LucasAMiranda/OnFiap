"""
with open("teste.txt", "w")as arquivo:
    conteudo = arquivo.read()
    arquivo.write("O parâmetro w cria um arquivo para dentro da pasta do projeto")


with open("teste.txt", "w") as arquivo:
    arquivo.write("sobrescrevendo o arquivo anterior")
"""

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "w") as arquivo:
    arquivo.write("Continuação do texto.")