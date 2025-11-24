print("Bem vindo ao nosso menu do Cefet;\n")
print("Responda algumas perguntas;")
print("De acordo com as suas respostas, vc terá acesso ao menu.")

idade = int(input("   Digite a sua idade por favor: "))
shopping_list = []

if idade < 18:
    anos_restantes = 18 - idade
    print(f"Voce é muito novo, volte daqui a {anos_restantes} anos.")
else:
    print("Pronto, a primeira pergunta já foi, agora temos outra pra voce.")

    palavra_secreta = "1BINFO"
    print("OBS: É a turma mais almejada do CEFET") 
    import time # Importado fora do loop

    max_tentativas = 5
    tempo_espera = 30
    tentativas_atuais = 0

    while True:
        palavra = input("   Digite a sua turma para ter acesso ao menu (em caps Lock)")

        if palavra == palavra_secreta:
            print("Parabéns, agora voce tem acesso ao menu")
            break
        else:
            tentativas_atuais += 1
            print("Turma não permitida. Tente novamente.")
            if tentativas_atuais >= max_tentativas:
                print(f"Número máximo de tentativas atingido. Aguarde {tempo_espera} segundos.")
                time.sleep(tempo_espera)
                tentativas_atuais = 0 # Reseta as tentativas após o tempo de espera

while True:
    print("\n MENU DE OPÇÕES")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - imprimir lista")
    print("4 - sair do programa")

    choice = input("Digite o número da opção desejada: ")

    if choice == '1':
        item = input("Digite o item a ser adicionado: ")
        shopping_list.append(item)
        print(f"'{item}' foi adicionado à lista.")
    elif choice == '2':
        if not shopping_list:
            print("A lista de compras está vazia. Não há itens para remover.")
            continue

        print("\n Itens na lista:")
        for i, item in enumerate(shopping_list):
            print(f"{i+1} - {item}")

        try:
            item_to_remove_index = int(input("Digite o número do item que deseja remover: ")) - 1
            if 0 <= item_to_remove_index < len(shopping_list):
                removed_item = shopping_list.pop(item_to_remove_index)
                print(f"'{removed_item}' foi removido da lista.")
            else:
                print("Número de item inválido. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    elif choice == '3':
        if not shopping_list:
            print("A lista de compras está vazia.")
        else:
            print("\n Sua lista de compras:")
            for i, item in enumerate(shopping_list):
                print(f"{i+1} - {item}")
    elif choice == '4':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
