import csv
import os
from Classes.Cliente import Cliente

ARQUIVO_CLIENTES = "Dados/clientes.csv"


def realizar_login():
    print("\n=== TELA DE LOGIN ===")
    email_login = input("Digite seu e-mail: ").strip()
    senha_login = input("Digite sua senha: ").strip()

    if not os.path.exists(ARQUIVO_CLIENTES):
        print("\nNenhum cliente cadastrado no sistema ainda.")
        return None

    with open(ARQUIVO_CLIENTES, mode="r", encoding="utf-8") as arquivo:
        # Lendo a primeira linha para descobrir se o separador é vírgula ou ponto e vírgula
        primeira_linha = arquivo.readline()
        separador = ';' if ';' in primeira_linha else ','

        # Voltamos o arquivo para o início para o DictReader conseguir ler tudo
        arquivo.seek(0)

        leitor = csv.DictReader(arquivo, delimiter=separador)

        for linha in leitor:
            # Tratamento para evitar que o programa quebre se o cabeçalho estiver desalinhado
            try:
                if linha["Email"].strip() == email_login and linha["Senha"].strip() == senha_login:
                    print("\nLogin realizado com sucesso!")
                    return Cliente(
                        nome=linha["Nome"],
                        email=linha["Email"],
                        telefone=linha["Telefone"],
                        endereco=linha["Endereco"],
                        senha=linha["Senha"]
                    )
            except KeyError:
                print("\nErro: O formato do arquivo de clientes está incorreto.")
                print("Por favor faça um novo cadastro.")
                return None

    print("\nE-mail ou senha incorretos!")
    return None