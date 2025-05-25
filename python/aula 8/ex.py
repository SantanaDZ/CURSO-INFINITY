class Fatura():
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0.0
        
    def GerarFatura(self):
        quantidade = max(0, self.quantidade)
        preco_unitario = max(0.0, self.preco_unitario)
        self.valor_total = quantidade * preco_unitario
        return  self.valor_total
    print(GerarFatura)    
fatura1 = Fatura('Teclado', 25.00, 6)   

valor = fatura1.GerarFatura()
print(f"Item: {fatura1.nome}")
print(f"Quantidade: {fatura1.quantidade}")
print(f"Preço unitário: R${fatura1.preco_unitario:.2f}")
print(f"Valor total da fatura: R${fatura1.valor_total:.2f}")