class Concessionaria:
    def __init__(self):
        self.estoque = []

    def adicionar_carro(self, carro):
        self.estoque.append(carro)

    def buscar_por_orcamento(self, orcamento):
        # Filtra os carros do estoque que custam menos ou o mesmo que o orçamento
        return [carro for carro in self.estoque if carro.preco <= orcamento]