import csv
import os
from Classes.Carro import Carro

ARQUIVO_ESTOQUE = "Dados/carros.csv"


def carregar_estoque(concessionaria):
    if not os.path.exists(ARQUIVO_ESTOQUE):
        print(f"Erro: Arquivo {ARQUIVO_ESTOQUE} não encontrado!")
        return

    with open(ARQUIVO_ESTOQUE, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            novo_carro = Carro(
                modelo=linha["Modelo"].strip(),
                marca=linha["Marca"].strip(),
                ano=linha["Ano"].strip(),
                preco=linha["Preco"].strip()
            )
            concessionaria.adicionar_carro(novo_carro)