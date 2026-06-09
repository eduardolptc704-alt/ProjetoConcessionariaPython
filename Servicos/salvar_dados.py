import csv
import os

# Caminho do arquivo onde os clientes são salvos
ARQUIVO_CLIENTES = "Dados/clientes.csv"

def salvar_cliente(cliente):
    # Verifica se o arquivo já existe para saber se precisa criar o cabeçalho
    arquivo_existe = os.path.isfile(ARQUIVO_CLIENTES)

    # Abre o arquivo no modo 'a' (append) para adicionar novos dados sem apagar os antigos
    with open(
        ARQUIVO_CLIENTES,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        if not arquivo_existe:
            escritor.writerow([
                "Nome",
                "Email",
                "Telefone",
                "Endereco",
                "Senha"
            ])

        escritor.writerow([
            cliente.nome,
            cliente.email,
            cliente.telefone,
            cliente.endereco,
            cliente.senha
        ])

    print("\nCadastro salvo com sucesso no banco de dados!")