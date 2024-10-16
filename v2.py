valor_total_pedido = 0
lista_carrinho = []

def cardapio():
    while True:
        print("Este é o nosso cardápio! Aproveite! 😜")
        print("-" * 20)
        print("[1] Salgados 🥐\n[2] Hamburger 🍔\n[3] Bebidas 🥤\n[4] Fechar 👋")
        entrada = input("Selecione uma das nossas opções: ")

        match entrada:
            case "1":
                salgados()
            case "2":
                burger()
            case "3":
                bebidas()
            case "4":
                print("\nAgradecemos a sua visita! \nEsperamos por você na próxima 😁")
                return
            case _:
                print("A Cleide Lanches não entendeu. Tente novamente!")
                print("-" * 20)

def calcular_total(carrinho):
    return sum(item["valor"] for item in carrinho)

def perguntar_se_deseja_continuar():
    while True:
        opcao = input("Deseja pedir mais alguma coisa? [SIM] ou [NÃO]: ")
        match opcao:
            case "SIM":
                return True
            case "NÃO":
                print("-" * 20)
                return False
            case _:
                print("Opção inválida. Tente novamente.")

def salgados():
    print("\nÓtima escolha!")
    print("[1] Pastel\n[2] Risólis\n[3] Enroladinho")
    entrada = input("Selecione uma das nossas opções: ")

    match entrada:
        case "1":
            pastel()
        case "2":
            risolis()
        case "3":
            lista_carrinho.append({"nome": "Enroladinho", "valor": 2.00})
            print("Você escolheu Enroladinho.")
        case _:
            print("Opção inválida.")
            salgados()

def pastel():
    print("\nOpções de Pastel: ")
    entrada = input("[1] Carne 🥩\n[2] Frango 🍗\n[3] Queijo 🧀  ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Pastel de Carne", "valor": 5.00})
            print("Você escolheu Pastel de Carne.")
        case "2":
            lista_carrinho.append({"nome": "Pastel de Frango", "valor": 5.00})
            print("Você escolheu Pastel de Frango.")
        case "3":
            lista_carrinho.append({"nome": "Pastel de Queijo", "valor": 5.00})
            print("Você escolheu Pastel de Queijo.")
        case _:
            print("Opção inválida.")

    processar_continuacao()

def risolis():
    print("\nOpções de Risólis: ") 
    entrada = input("[1] Carne 🥩\n[2] Frango 🍗  ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Risólis de Carne", "valor": 4.00})
            print("Você escolheu Risólis de Carne.")
        case "2":
            lista_carrinho.append({"nome": "Risólis de Frango", "valor": 4.00})
            print("Você escolheu Risólis de Frango.")
        case _:
            print("Opção inválida.")

    processar_continuacao()

def burger():
    print("\nOpções de Hamburger: ")
    entrada = input("[1] Super Cleide 😱\n[2] Big Cleide 😎\n[3] Veg Cleide 🥗 ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Super Cleide", "valor": 23.00})
            print("Você escolheu Super Cleide.")
        case "2":
            lista_carrinho.append({"nome": "Big Cleide", "valor": 18.00})
            print("Você escolheu Big Cleide.")
        case "3":
            lista_carrinho.append({"nome": "Veg Cleide", "valor": 20.00})
            print("Você escolheu Veg Cleide.")
        case _:
            print("Opção inválida.")

    processar_continuacao()

def bebidas():
    print("\nOpções de Bebidas: ")
    print("[1] Pepsi\n[2] Fanta\n[3] Guaraná\n[4] Sprite\n[5] Tap Water")
    entrada = input("Escolha uma bebida: ")

    match entrada:
        case "1" | "2" | "3" | "4":
            lista_carrinho.append({"nome": "Refrigerante", "valor": 5.00})
            print("Você escolheu Refrigerante Lata. 🥃")
        case "5":
            lista_carrinho.append({"nome": "Água", "valor": 3.00})
            print("Você escolheu Tap Water. 🧊")
        case _:
            print("Opção inválida.")
            bebidas()

    processar_continuacao()

def processar_continuacao():
    if not perguntar_se_deseja_continuar():
        if confirmar_pedido(lista_carrinho):
            checkout(lista_carrinho)

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

    confirmar = input("Deseja confirmar o pedido? [SIM] ou [NÃO]: ")
    if confirmar == "SIM":
        checkout(lista_carrinho)
    elif confirmar == "NÃO":
        print("Pedido não confirmado. Obrigado!")
        return  # Retorna sem chamar o cardápio

def checkout(lista_carrinho):
    print("\nIniciando checkout...")
    total = calcular_total(lista_carrinho)
    print(f"Valor total do checkout: R$ {total:.2f}")
    metodo_de_pagamento = int(input("\nQual método de pagamento você deseja?\n-------\n 1-Pix \n-------\n 2-Dinheiro\n-------\n 3-Cartão \n------> "))
    
    if metodo_de_pagamento == 1:
        print("⬛⬜⬛⬛⬜\n⬜⬜⬛⬜⬛\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜")
        final()
    elif metodo_de_pagamento == 2:
        print("Vá ao caixa e realize o pagamento!")
        final()
    elif metodo_de_pagamento == 3:
        print("Funcionalidade de pagamento com cartão ainda não implementada.")
        final()

import time
import random
import webbrowser

def final():
    print(f"\nPedido realizado com sucesso! O número do seu pedido é: {random.randint(0, 999)}")
    segundos = 59
    minutos = random.randint(3, 6)

    while minutos >= 0:
        if segundos > -1:
            print(minutos, ":", segundos)
            segundos -= 1
            time.sleep(0.01)  # Aumentei o tempo para 1 segundo para ser mais realista
        if segundos == -1:
            segundos = 59
            minutos -= 1

    print("\nA comida está pronta!")
    webbrowser.open("https://www.youtube.com/shorts/ZjEJaWByFlY")

# Chamada inicial ao cardápio
cardapio()