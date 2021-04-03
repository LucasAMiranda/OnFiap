def chamarMenu():
    escolha = int(input("Digite: "
                    
"<1>Para registrar ativo"
                
"<2>Para persistir arquivo"
                     
"<3>Para exibir ativos armazenado"))
    return escolha


def registrar(dicionario):
    resp= "S"
    while resp=="S":
        dicionario[input("Digit o número patrimonial")] = [
        input("Digite a data da última atualização:"),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave,  valor in dicionario.items():
            inv.write(chave + ";" +valor[0] + ";" +
                    valor[1] + ";" +valor[2]+ "")

    return "Persistindo com sucesso"

def exibir(dicionario):
    with open("inventario.csv",  "a")as inv:
        linhas = inv.readlines()
    return linhas
