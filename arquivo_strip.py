arquivo = open ("strip.txt", "r+")
linhas = arquivo.readlines()

arquivo = open ("strip.txt", "w")
for linha in linhas:
    arquivo.write(linha.strip()+"\n")

arquivo.close()




#message = '      banana\npera        \n   caju'
#print (message.strip())
#arquivo.close()

#arquivo = open ("strip.txt", "w")
#arquivo.write (message)

