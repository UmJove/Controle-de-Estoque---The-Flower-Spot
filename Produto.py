class Produto:
    def __init__ (self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    #métodos
    def rg_chegada_de_insumo(self, data_recebimento, quantidade_recebida):
        # lotes = {}
        # data_recebimento = input(f"Data recebimento: ")
        # quantidade_recebida = int(input(f"Quantidade ({self.nome}) recebida: "))
        self.quantidade += quantidade_recebida
        print(f"Quantidade de {self.nome} (ID = {self.id}) atualizada: {self.quantidade} -- RG {data_recebimento}")

    def promocao(self, porcentagem_desconto):
        preco_promocao = self.preco - (porcentagem_desconto*self.preco/100)
        return f"{preco_promocao:.2f}"

    # verificar estoque e necessidade de repor

    #Getters e Setters
    def get_id(self):
        return self.id
    
    def set_id(self, novo_id):
        try:
            self.id = int(novo_id)
            return True
        except ValueError:
            print ("id inválido, use apenas números inteiros")
            return False
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return True
        # novo_id = int(input("Digite o id que deseja atribuir ao produto")

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return True

    def get_quantidade(self):
        return self.quantidade
    
    def set_quantidade(self, novo_quantidade):
        self.quantidade = novo_quantidade
        return True




if __name__ == "__main__":
    produto_teste = Produto(1, "Tulipas", 22.50, 10)
    # produto_teste.chegada_de_insumo()
    print(produto_teste.promocao(10))

