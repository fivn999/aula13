entrada = input("Qual poesia voce está pensando hoje? ")
arquivo = open("poesias.txt", "a")
arquivo.write(entrada +"\n")
arquivo.close()

while True:
    opcao = input("Deseja adicionar mais uma poesia? ")
    if opcao == "nao":
        print ("Agradecemos o seu tempo! Até logo.")
        break
    elif opcao == "sim":
        entrada = input("escreva a poesia? ")
        arquivo = open("poesias.txt", "a")
        arquivo.write(entrada +"\n")
        arquivo.close()
    else:
        print ("Está confuso? Não entendi")    