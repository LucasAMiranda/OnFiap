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

serial = input("Digite o serial do equipamento que será excluído: ")
for indice in range(0, len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print("Equipamento...: ", (indice + 1))
    print("NOME.........:", equipamentos[indice])
    print("VALOR.........:", valores[indice])
    print("SERIAL.........:", seriais[indice])
    print("DEPARTAMENTO.........:", departamentos[indice])