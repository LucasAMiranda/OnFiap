#elaborar o código para resolver a seguinte situação:
# o seu módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa,
# caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres.
# Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres. Se o nível for GUEST,
# a mensagem deverá ser “Olá visitante”. E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir a mensagem “Olá desconhecido(a)”.
# Considere apenas os gêneros masculino e feminino e não olhe o código abaixo, até resolver o seu desafio.

nivelAcesso = input("informe o nivel de acesso: ").upper()

if nivelAcesso == "ADM" or nivelAcesso == "USR":
    genero = input("Informe o gênero: ").upper()
    if nivelAcesso == "ADM":
        if genero == "FEMININO":
           print("Olá administradora")
        else:
           print("Olá administrador")

    else:
         if genero == "FEMININO":
             print("Olá Usuária")
         else:
             print("Olá Usuário")

elif nivelAcesso == "GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
