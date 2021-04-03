texto = "eu amo python"

#método find encontra um caractere ou uma string que queremos percorrer

print(texto.find("o"))
print(texto[texto.find("o")+1:].find("o"))

#método split : serve para cortar um  caractere no texto em string , mas no nosso exemplo vamos querer que não seja  cortado nada.
#Retorna o texto em forma de lista

print(texto.split(" "))