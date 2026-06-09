class Carro:
    # Construtor da classe com o preço encapsulado
    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = int(ano)
        self.__preco = float(preco)  # Atributo privado

    # GETTER: Permite que o sistema leia o preço de forma limpa usando 'carro.preco'
    @property
    def preco(self):
        return self.__preco

    # SETTER: Protege o preço contra valores inválidos na hora da alteração
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = float(novo_preco)
        else:
            print("❌ Erro de Segurança: O preço do veículo deve ser maior que zero!")