with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1>Esta é uma página teste para web</h1></body>")
    pagina.write("<br><h2>Abaixo segue alguns nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome !="Sair":
        nome  = input("Digite um nome ou SAIR: ").upper()

        if nome != "Sair":
            pagina.write("<br> " + nome)
    pagina.write("</h3></body>")