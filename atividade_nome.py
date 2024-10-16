import os

# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for nome, tel, mail, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")
            f.write(f"{tel}: {valor}\n")
            f.write(f"{mail}: {valor}\n")

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
            variaveis_carregadas = carregar_variaveis('dados.txt')

            if len(variaveis_carregadas) == 0:
                print(f"seja bem vindo novamente {variaveis_carregadas["nome"]}")
            else:
                nome_v = input("Qual o seu nome?")
                salvar_variaveis('dados.txt',nome = nome_v )
                telefone_v = input("Qual o seu telefone?")
                salvar_variaveis('dados.txt',tel = telefone_v )
                email_v = input("Qual o seu telefone?")
                salvar_variaveis('dados.txt',mail = email_v )

        case False:
            nome_v = input("por favor digite seu nome")
            salvar_variaveis('dados.txt',nome = nome_v )

verifica_primeira_vez()