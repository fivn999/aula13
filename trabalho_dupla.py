valor_total_pedido = 0
lista_carrinho = []

def cardapio():
    while True:
        print("Este é o nosso cardápio! Aproveite! 😜")
        print("-" * 20)
        print("[1] Salgados 🥐\n[2] Hamburger 🍔\n[3] Bebidas 🥤\n[4] Fechar 👋")
        entrada = input("Selecione uma das nossas opções: ")

        if entrada == "1":
            menu_itens("Salgados", ["Pastel", "Risólis", "Enroladinho"], [5.00, 4.00, 2.00])
        elif entrada == "2":
            menu_itens("Hamburgers", ["Super Cleide", "Big Cleide", "Veg Cleide"], [23.00, 18.00, 20.00])
        elif entrada == "3":
            menu_itens("Bebidas", ["Refrigerante", "Água"], [5.00, 3.00])
        elif entrada == "4":
            print("\nAgradecemos a sua visita! \nEsperamos por você na próxima 😁")
            return
        else:
            print("A Cleide Lanches não entendeu. Tente novamente!")

        if confirmar_pedido(lista_carrinho):
            total = calcular_total(lista_carrinho)
            print(f"Seu pedido foi confirmado e o valor total ficou de: R$ {total:.2f}")
            lista_carrinho.clear()

def calcular_total(carrinho):
    return sum(item["valor"] for item in carrinho)

def perguntar_se_deseja_continuar():
    while True:
        opcao = input("Deseja pedir mais alguma coisa? [SIM] ou [NÃO]: ").strip().upper()
        if opcao in ["SIM", "NÃO"]:
            return opcao == "SIM"
        else:
            print("Opção inválida. Tente novamente.")

def menu_itens(tipo, nomes, precos):
    print(f"\nÓtima escolha! Opções de {tipo}:")
    for i, (nome, preco) in enumerate(zip(nomes, precos), 1):
        print(f"[{i}] {nome} (R$ {preco:.2f})")
    
    entrada = input("Selecione uma das nossas opções: ")
    
    if entrada.isdigit() and 1 <= int(entrada) <= len(nomes):
        item = nomes[int(entrada) - 1]
        valor = precos[int(entrada) - 1]
        lista_carrinho.append({"nome": item, "valor": valor})
        print(f"Você escolheu {item}.")
    else:
        print("Opção inválida.")
    
    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def confirmar_pedido(lista_carrinho):
    if lista_carrinho:
        print("Você escolheu:")
        for item in lista_carrinho:
            print(f"- {item['nome']} (R$ {item['valor']:.2f})")
        total = calcular_total(lista_carrinho)
        print(f"Total do pedido: R$ {total:.2f}")
    else:
        print("Você não fez nenhum pedido.")
        return False

    while True:
        confirmar = input("Deseja confirmar o pedido? [SIM] ou [NÃO]: ").strip().upper()
        if confirmar in ["SIM", "NÃO"]:
            return confirmar == "SIM"
        else:
            print("Opção inválida. Tente novamente.")

cardapio()
