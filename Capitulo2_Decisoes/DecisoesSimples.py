#Algoritmo do atendimento prioritário de idade miníma de até 65 anos
#Entrada: Nome, Idade, Prioritário
#Processamento : Se o paciente tem idade maior ou igual a 65 anos de idade
#Saída: Mostrar o nome e a  idade do paciente e se ele pode ser atendido ou não.

# #ATENÇÃO: Nunca substitua condições compostas usando if / else por duas ou mais condições simples
#Observe o seguinte: se o paciente tiver 80 anos, o primeiro “if” será processado, mesmo assim,
# a linguagem verificará o segundo “if”,
# e sabemos que não existe chance alguma de a condição do segundo “if” ser verdadeira,
# ou seja, a linguagem vai consumir um processamento desnecessário.

nome = input("Nome do paciente: ")
idade = int(input("Qual a idade do paciente? : "))
prioridade = "NÃO"

if idade >= 65:
    prioridade = "SIM"
print("O paciente de nome " + nome + " possui atendimento prioritário: " + prioridade)


'''
NUNCA USE ASSIM OU FAÇA ISSO ESTÁ ERRADO

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
if idade < 65:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
'''