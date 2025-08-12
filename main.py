carrinho = {}
dados_do_pedido = {}
endereço = {}

# lotes = {} #Possível funcionalidade atrelada ao método rg_chegada_de_insumo()
# data_recebimento = input(f"Data recebimento: ")
# quantidade_recebida = int(input(f"Quantidade ({self.nome}) recebida: "))

produtos = {
    1: {"nome": "Buquê com 3 Rosas Brancas", "preco": 100.00, "Quantidade": 20},
    2: {"nome": "Buquê com 3 Rosas vermelhas", "preco": 100.0, "Quantidade": 20},
    3: {"nome": "Buquê com 3 Rosas cor de Rosa", "preco": 100.00, "Quantidade": 20},
    4: {"nome": "Buquê Mix de Flores M (colorido)", "preco": 220.00, "Quantidade": 20},
    5: {"nome": "Buquê Paris", "preco": 380.00, "Quantidade": 20}
}

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço do produto (ex: 199.90): "))
        quantidade = int(input("Quantidade em estoque: "))

        # Gerar novo ID automático baseado no maior ID atual
        novo_id = max(produtos.keys(), default=0) + 1

        produtos[novo_id] = {
            "nome": nome,
            "preco": preco,
            "Quantidade": quantidade
        }

        print(f"\nProduto '{nome}' cadastrado com sucesso com ID {novo_id}!")
    except ValueError:
        print("Erro: Entrada inválida. Tente novamente com os dados corretos.")

def editar_produto():
    listar_produtos()
    try:
        id = int(input("\nDigite o ID do produto que deseja editar: "))
        if id in produtos:
            print(f"Editando produto: {produtos[id]['nome']}")
            novo_nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
            novo_preco = input("Novo preço (deixe em branco para manter o atual): ").strip()
            nova_qtd = input("Nova quantidade (deixe em branco para manter a atual): ").strip()

            if novo_nome:
                produtos[id]['nome'] = novo_nome
            if novo_preco:
                produtos[id]['preco'] = float(novo_preco)
            if nova_qtd:
                produtos[id]['Quantidade'] = int(nova_qtd)

            print("Produto atualizado com sucesso.")
        else:
            print("Produto com esse ID não encontrado.")
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

def listar_produtos():
    print("\nProdutos disponíveis:")
    for id, info in produtos.items():
        print(f"{id}: {info['nome']} - R${info['preco']:.2f}")


def menu(): # escolher usuário antes de dar opções (comprador(opções 1, 2, 3, 4, 5, 9), funcionário (opções 1, 6, 7, 8, 9) )
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos")
        print("2. Cadastrar novo produto (somente pessoas autorizadas)") # add ver com quantidades atualizadas em estoque
        print("3. Editar produto (somente pessoas autorizadas)")     
        print("4. Excluir produto (somente pessoas autorizadas)")
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

def inicio():
    print("\nSeja bem-vindo à 'The Flower Spot', sua floricultura digital!")
    menu()
    
def sair():
    print("Encerrando o sistema. Até logo!")
    exit()

# Iniciar o sistema
inicio()
