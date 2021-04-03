def perguntar():
    return input("O que deseja realiza?\n" +
                 "<I> - Para inserir um usuário\n" +
                 "<P> - Para pesquisar um usuário\n" +
                 "<E> - Para excluir un usuário\n" +
                 "<L> - Para Listar um usuário: " ).upper()

def inserir(dicionarios):
    dicionarios[input("Digite  o login: ").upper()] = [input("Digite o nome").upper(),
                                                       input("Digite o último dia de acesso: "),
                                                       input("Qual a última estação acessada: ").upper()]
    salvar(dicionarios)

def salvar(dicionarios):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionarios.items():
            arquivo.write(chave+ " : " +str(valor))


def pesquisar(dicionarios, chave):
    lista = dicionarios.get(chave)
    if lista != none:
        print("Nome........: "  +list[0])
        print("Último acesso:"  +lista[1])
        print("Última estação:" +lista[2])

def excluir(dicionarios,chave):
    if dicionarios.get(chave)!=none:
        del dicionarios[chave]
        print("Objeto Elimindado")

def listar(dicionarios):
    for chave, valor in dicionarios.items():
        print("Objeto........")
        print("Login: ", chave)
        print("Dados: ", valor)