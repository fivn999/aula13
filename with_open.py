# Abrindo um arquivo para escrita
with open('exemplo.txt', 'w', encoding = 'utf-8') as arquivo: #Usando o "ENCONDING = 'UTF-8' consigo colocar acentos no arquivo sem bugar."
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo do uso de with.') #Ao usar o "WITH" eu nao preciso usar o comando de CLOSE no arquivo, oq faz o codigo ficar mais simples!

# O arquivo é automaticamente fechado após o bloco with
    
  
arquivo.seek(0) # Usamos o "SEEK (0)" para mover o cursor de volta ao início do arquivo
   
    
conteudo = arquivo.read() #Ler e imprimir o conteúdo do arquivo
print(conteudo)

