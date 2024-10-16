def funcao (**kwargs):
    for var, value in kwargs.items():
        print (f"{var}: {value}")

funcao (nome="alice", idade=30, cidade="SP")

#Usando o **KWARGS consigo executar a função sem determinar um numero de parametros.
# o KWARGS pode ser feito com qualquer nome de variavel, sendo antecedido por dois asteriscos ** 
