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

# Todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo período) de 10%.
depreciacao = input("Entre com o nome do equipamento que será depreciado: ")

for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor Antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.10
        print("O Novo valor: ", valores[indice])
