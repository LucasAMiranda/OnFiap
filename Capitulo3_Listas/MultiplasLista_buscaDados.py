# DECLARANDO AS VARIÁVEIS
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()

# Pesquisando e Inserindo um determinado Dado dentro da lista

busca = input("Entre com o nome do equipamento que deseja buscar: ")

for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("VALOR...: ", valores[indice])
        print("SERIAL...: ", seriais[indice])
