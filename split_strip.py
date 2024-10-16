string = " chave1 : valor1 ,  chave2 : valor2 ,  chave3 : valor3 "

lista = string.strip().split(": ")

chave1 = lista [0].split()[0].strip()
valor1 = lista[1].split(",")[0].strip()
print(chave1)
print (valor1)

chave2 = lista [1].split()[2].strip()
valor2 = lista[2].split(",")[0].strip()
print(chave2)
print (valor2)


chave3 = lista [2].split()[2].strip()
valor3 = lista[3].split(",")[0].strip()
print(chave3)
print (valor3)


