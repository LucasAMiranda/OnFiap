'''
nome = "Lucas Alencar Miranda"
empresa = "LSchoolinfotech"
qtdFuncionarios = 0
media_salarial = 1.500
print(nome + " trabalha na empresa " + empresa)
print("Possui " + str(qtdFuncionarios) + " funcionários")
print("A média salarial é de: " + str(media_salarial))
'''
'''
nome = input("Digite o nome do Funcionário: ")
empresa = input("Digite a instituição trabalhada: ")
qtdFuncionarios = int( input("Digite a quantidade de funcionários: "))
media_salarial = float(input("Digite a media salarial: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui " + str(qtdFuncionarios) + " funcionários")
print("A média salarial é de: " + str(media_salarial))
'''

nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))