#Definição de variáveiss

ips={ }
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo os Ip's: ") #retorna como saída a chave dos ips
for ip in ips.keys():
    print(ip[0] + "." + ip[1]) #A saída são os dois primeiros octetos do ip e os dois últimos

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1] == pesquisa):
        print(nome)

print("Exibindo máquinas com o mesmo endereço: ")
rede = input("Digite os primeros octetos: ")
for ip, nome in ips.items():
    if(ip[0]==rede):
        print(nome)