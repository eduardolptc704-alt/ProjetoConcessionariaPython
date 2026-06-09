import csv
import os
from Classes.Cliente import Cliente

ARQUIVO_CLIENTES = "Dados/clientes.csv"


def cadastrar_cliente():
    print("\n=== CADASTRO DE CLIENTE ===\n")

    email = input("Digite seu e-mail: ").strip()

    # Validação para evitar e-mails duplicados
    if os.path.exists(ARQUIVO_CLIENTES):
        with open(ARQUIVO_CLIENTES, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            # Lê a primeira linha para identificar o delimitador correto
            arquivo.seek(0)
            linha1 = arquivo.readline()
            separador = ';' if ';' in linha1 else ','
            arquivo.seek(0)

            leitor = csv.DictReader(arquivo, delimiter=separador)
            for linha in leitor:
                if linha["Email"].strip() == email:
                    print("\n❌ Este e-mail já está cadastrado! Tente fazer o login.")
                    return None  # Retorna None para o main tratar

    nome = input("Como gostaria de ser chamado? ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")
    senha = input("Crie uma senha de acesso: ")

    return Cliente(nome, email, telefone, endereco, senha)