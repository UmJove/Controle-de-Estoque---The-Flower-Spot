from Produto import Produto

p1 = Produto(1, "Rosas Brancas", 24.90, 20)
p2 = Produto(2, "Rosas Vermelhas", 29.90, 10)
p3 = Produto(3, "Tulipa", 34.90, 20)
p4 = Produto(4, "Girassol", 14.90, 10)

produtos = [p1,p2,p3,p4]
estoque_dados = {}

def menu(): 
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos em estoque")
        print("2. Cadastrar novo produto") # add ver com quantidades atualizadas em estoque
        print("3. Editar produto")     
        print("4. Excluir produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

def listar_produtos():
    print("\nProdutos disponíveis em estoque:")
    for produto in produtos:
        print(f"ID {produto.id} - {produto.nome} - R$ {produto.preco:.2f} - {produto.quantidade} unidades")

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço do produto (ex: 19.90): "))
        quantidade = int(input("Quantidade em estoque: "))

        # Gerar novo ID automático baseado no maior ID atual
        novo_id = (len(produtos) + 1)
        novo_produto = Produto(novo_id, nome, preco, quantidade)
        
        produtos.append(novo_produto)

        ## Uppar dados (posteriorment em json)
        estoque_dados[novo_produto.id] = {"nome":novo_produto.nome, "preço":novo_produto.preco, "quantidade":novo_produto.quantidade}
        print(f"\nProduto cadastrado \nID {novo_produto.id} - {estoque_dados[novo_produto.id]}!")

    except ValueError:
        print("Erro: Entrada inválida. Tente novamente com os dados corretos.")

def editar_produto():
    listar_produtos()
    try:
        id_input = int(input("\nDigite o ID do produto que deseja editar: "))
        for produto in produtos:
            if produto.id == id_input:
                print(f"Editando produto: ID {produto.id} - {produto.nome}")
                novo_nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
                novo_preco = input("Novo preço (deixe em branco para manter o atual): ").strip()
                nova_qtd = input("Nova quantidade (deixe em branco para manter a atual): ").strip()

                if novo_nome:
                    produto.nome = novo_nome
                if novo_preco:
                    produto.preco = float(novo_preco)
                if nova_qtd:
                    produto.quantidade = int(nova_qtd)

                print("Produto atualizado com sucesso.")

    except ValueError:
        print("Entrada inválida. Tente novamente.")



def excluir_produto():
    listar_produtos()
    try:
        id = int(input("\nDigite o ID do produto que deseja excluir: "))
        if id in produtos:
            confirmacao = input(f"Tem certeza que deseja excluir '{produtos[id]['nome']}'? (s/n): ")
            if confirmacao.lower() == 's':
                del produtos[id]
                print("Produto excluído com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Produto com esse ID não encontrado.")
    except ValueError:
        print("Entrada inválida.")





def inicio():
    print("\nSeja bem-vindo à 'The Flower Spot', sua floricultura digital!")
    menu()
    
def sair():
    print("Encerrando o sistema. Até logo!")
    exit()

# Iniciar o sistema
inicio()
