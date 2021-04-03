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

# PERCORRENDO TODAS AS FAIXAS DOS EQUIPAMENTOS DENTRO DA LISTA E GUARDANDO CADA VALOR DENTRO DO ÍNDICE DA LISTA
for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice + 1))
    print("NOME.........:", equipamentos[indice])
    print("VALOR.........:", valores[indice])
    print("SERIAL.........:", seriais[indice])
    print("DEPARTAMENTO.........:", departamentos[indice])


