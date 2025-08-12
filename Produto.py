import time

class Produto:
    def __init__ (self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def verificar_quantidade(self):
        return 

class Flor(Produto):
    def __init__(self, id, nome, preco, quantidade,tempo_vida,data_colheita):
        super().__init__(id, nome, preco, quantidade)
        self.tempo_vida=tempo_vida
        self.data_colheita=data_colheita
        

    

    def verificar_viabilidade_entrega(self,data_entrega):
        colheita=time.strptime(self.data_colheita,"%d/%m/%Y")
        colheita_segundos=time.mktime(colheita)
        validade_segundos=colheita_segundos+((self.tempo_vida)*60*60*24)
        entrega=time.strptime(data_entrega,"%d/%m/%Y")
        entrega_segundos=time.mktime(entrega)
        if entrega_segundos>validade_segundos:
            print("Não é possivel fazer a entregar")
        else:
            dias=int((validade_segundos-entrega_segundos)/(60*60*24))
            print(f"A entregar viavel dias {dias}")

f1=Flor("Rosa Vermelha",10,5,1,10,"05/08/2025")
f1.verificar_viabilidade_entrega("16/08/2025")