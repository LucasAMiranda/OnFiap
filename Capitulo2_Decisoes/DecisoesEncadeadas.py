nome  = input("Digite seu nome : ")
idade = int(input("Digite sua idade: "))
doenca_contagiosa = input("Supeita de doença infecto-contagiosa? : ").upper()
if idade >= 65:
    print("O paciente tem prioridade de atendimento médico.")

    if doenca_contagiosa == "SIM":
        print("Encaminhe o paciente para a sala AMARELA ")
    elif doenca_contagiosa == "NÃO":
        print("Encaminhe o paciente para sala Branca")
    else:
        print("Responda a pergunta de doença infecto-contagiosa com SIM ou NÃO")

else:
    print("O paciente não tem prioriridade de atendimento médico.")

    if doenca_contagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_contagiosa == "NÃO":
        print("Encaminhe o paciente para sala Branca")
    else:
        print("Responda a pergunta de doença infecto-contagiosa com SIM ou NÃO")

