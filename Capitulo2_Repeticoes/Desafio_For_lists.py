inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(input("Setor: "))
    inventario.append(input("Número Serial: "))
    resposta = input("Deseja \"S\" continuar: ").upper()

for equipamentos in inventario:
    print(equipamentos)
