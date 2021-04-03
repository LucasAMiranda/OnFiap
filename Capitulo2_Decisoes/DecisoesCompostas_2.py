# ALGORITMO:  imaginar que pessoas com idade igual ou superior a 65 receberão atendimento prioritário, mas que também
# pessoas com suspeita de doenças infecto-contagiosas deverão ser direcionadas para uma sala de espera distinta,
# por motivos óbvios.

# Entrada: Nome, Idade, doenca_contagiosa
# Processamento : Se o paciente tem idade maior ou igual a 65 anos de idade, senão verifica ser doente contagioso
# Saída: Mostrar o nome e a  idade do paciente e se ele pode ser atendido ou não.

nome = input("Digite seu nome aqui: ")
idade = int(input("Digite sua idade aqui: "))
doenca_contagiosa = input("Suspeita de doença infecto-contagiosa? : ").upper()

if idade >= 65:
    print("O pacinte " + nome + " possui atendimento prioritário!")
elif doenca_contagiosa == "SIM":
    print("O paciente será direcionado para uma sala de espera reservada.")
else:
    print("O(A) paciente " + nome + " não tem idade para atendimento prioritário. Favor aguarde na sala comum! ")

# ATENÇÃO: função chamada “upper()”. Esta função tem a finalidade de converter o conteúdo de uma string para letras
# maiúsculas, ou seja, o que for digitado no “input()”, pelo usuário final, será convertido para caixa alta (letras
# maiúsculas), assim fica mais fácil realizar a comparação na condição dentro do “if”.
