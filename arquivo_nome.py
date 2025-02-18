import os

# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for nome, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(path_file):
    variaveis = {}
    with open(path_file, 'r') as f:
        for line in f:
            nome, valor = line.strip().split(': ')
            variaveis[nome] = valor
    return variaveis

def verifica_primeira_vez():
    match os.path.exists("variaveis.txt"):

        case True:
            variaveis_carregadas = carregar_variaveis('variaveis.txt')

            if len(variaveis_carregadas) > 0:
                print(f"seja bem vindo novamente {variaveis_carregadas["nome"]}")
            else:
                nome_v = input("por favor digite seu nome")
                salvar_variaveis('variaveis.txt',nome = nome_v )
        case False:
            nome_v = input("por favor digite seu nome")
            salvar_variaveis('variaveis.txt',nome = nome_v )

verifica_primeira_vez()