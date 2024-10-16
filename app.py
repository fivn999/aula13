#open("caminho","r")

#Mode
#r - Leitura
#a - Append
#w - Escrita
#x - Criar Arquivo
# r+ - Leitura + Escrita


#arquivo = open("teste.txt", "a") #A letra "A" incrementa um novo item na lista txt, ja as letras "W" e "R+" apaga todos os itens e reescreve somente o novo item.

#lista = arquivo.readlines() #"READLINES" transforma as linhas do arquivo em uma lista

#arquivo.write("\nSQL")

#print(lista)

import os

if os.path.exists ("novo_teste.txt"):
    os.remove ("novo_teste.txt")

else:
    print ("Nao existe")


#arquivo = open("novo_teste.txt", "a")
#arquivo.close()